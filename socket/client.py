import socket

def setIP():
    #HOST = ' 10.0.0.1' # According to your server ip address
    HOST = '140.112.149.69'
    PORT = 30036 # The same port as used by the server
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    return s

def parseData():
    f = open('input.txt', 'r')
    sourceInLines = f.readlines()  
    f.close()                                  
    for line in sourceInLines:
        temp1 = line.strip('\n')
    return temp1 
      
if __name__ == '__main__':
    old = parseData()
    s = setIP()
    print 'Send : ', str(old)
    s.sendall(old)
    data = s.recv(1024)
    file = open('r03943087.txt', 'w')
    file.write(data)
    file.close
    s.close()
    print 'Received :', str(data)
