from mininet.topo import Topo
from mininet.net import Mininet
from mininet.node import CPULimitedHost
from mininet.link import TCLink
from mininet.log import setLogLevel
from mininet.cli import CLI

class CustomTopo(Topo):
    "Simple Data Center Topology"

    "linkopts - (1:core, 2:aggregation, 3: edge) parameters"
    "fanout - number of child switch per parent switch"
    def __init__(self, linkopts1, linkopts2, linkopts3, fanout=2, **opts):
        # Initialize topology and default options
        Topo.__init__(self, **opts)

        # Add your logic here ...
        self.fanout = fanout
        core = self.addSwitch('C1')
        for i in xrange(fanout):
            aggregation = self.addSwitch('A%s' %(i + 1))
            self.addLink(core, aggregation, **linkopts1)
            for j in xrange(fanout):
                edge = self.addSwitch('E%s' %(fanout * i + j + 1))
                self.addLink(aggregation, edge, **linkopts2)
                for k in xrange(fanout):
                    host = self.addHost('h%s' %((fanout * (fanout * i + j)) + k + 1))
                    self.addLink(edge, host, **linkopts3)
      
#Function used to "test/verify" your topo
def perfTest():
   "Create network and run simple performance test"
   #"--- core to aggregation switches"
   linkopts1 = {'bw':50, 'delay':'5ms'}
   #"--- aggregation to edge switches"
   linkopts2 = {'bw':30, 'delay':'10ms'}
   #"--- edge switches to hosts"
   linkopts3 = {'bw':10, 'delay':'15ms'}
   topo = CustomTopo(linkopts1 , linkopts2 , linkopts3 , fanout= 2)
   net = Mininet(topo=topo, host=CPULimitedHost, link=TCLink)
   net.start()
   CLI(net)
   net.stop()

topos = { 'custom': ( lambda: CustomTopo() ) }

#Main function used to conduct the test
if __name__ == "__main__":
 setLogLevel('info')
 perfTest()

