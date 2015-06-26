import argparse
import math
import sys
import time
from fibonacci_heap_mod import Fibonacci_heap

dictnode = {}
dictgraph = {}
listInput = []
shortestpath = []

class Heap(dict):
    def __init__(self,):
        self.itemlist = []
        self.heap = Fibonacci_heap()

    def __setitem__(self, key, priority):
        if type(priority) is not int and type(priority) is not float:
            raise TypeError, "priority type is " + str(type(priority))
        if key in self.itemlist:
            if self[key] < priority:
                raise ValueError, "priority cannot be increase."
            else:
                entry = super(Heap, self).__getitem__(key)
                self.heap.decrease_key(entry, priority)
        else:
            self.itemlist.append(key)
            super(Heap, self).__setitem__(key, self.heap.enqueue(key, priority))

    def __getitem__(self, key):
        entry = super(Heap, self).__getitem__(key)
        return entry.get_priority()

    def __iter__(self):
        while self.heap.__len__() != 0:
            entry  = self.heap.dequeue_min()
            yield entry.get_value()
            self.itemlist.remove(entry.get_value())
            super(Heap, self).pop(entry.get_value())

def usage():
    print "Usage: python FindPath.py [D/B] [START] [DESTINATION]" 
    sys.exit(0);

def distance(a, b, c, d):
    return math.sqrt((a-c)**2 + (b-d)**2)

def readFile():
    f = open("usa.txt", "r")
    sourceline = f.readline().split()     
    for i in xrange(int(sourceline[0])):
        dictgraph[i] = {}
    for line in f:
        word = line.split()
        if len(word) is 3:
            dictnode[int(word[0])] = [float(word[1]), float(word[2])]
        elif len(word) is 2:
            a, b = int(word[0]), int(word[1])
            node1, node2 = dictnode[a], dictnode[b]
            dictgraph[a][b] = distance(node1[0], node1[1], node2[0], node2[1])
            dictgraph[b][a] = distance(node1[0], node1[1], node2[0], node2[1])
        else:
            pass
    f.close()
    listInput = [dictgraph, int(sourceline[0]), int(sourceline[1])]
    return listInput
 
def Dijkstra(graph, source, destination):
    dictfinaldistance = {}
    dictpredecessor = {}
    dictpriority = Heap() 
    dictpriority[source] = 0

    for i in dictpriority:
        dictfinaldistance[i] = dictpriority[i]
        if i == destination:
            break
        for j in graph[i]:
            ijLength = dictfinaldistance[i] + graph[i][j]
            if j in dictfinaldistance:
                pass
            elif j not in dictpriority or ijLength < dictpriority[j]:
                dictpriority[j] = ijLength
                dictpredecessor[j] = i
    return (dictfinaldistance[destination], dictpredecessor)

def BellmanFord(graph, source, destination):
    tempd = {}
    tempp = {}
    Q = []
    R = {}
    for node in graph:
        tempd[node] = float("Inf")
        tempp[node] = None
    tempd[source] = 0
    dictfinaldistance = tempd
    dictpredecessor = tempp 
    Q.append(source)
    R[source] = True
    while len(Q) != 0:
        i = Q.pop(0)
        del R[i]
        for j in graph[i]:
            if dictfinaldistance[j] > dictfinaldistance[i] + graph[i][j]:
                dictfinaldistance[j] = dictfinaldistance[i] + graph[i][j]
                dictpredecessor[j] = i
                if j not in R:
                    Q.append(j)
                    R[j] = True
    return (dictfinaldistance[destination], dictpredecessor)
    
if __name__ == "__main__":
    starttime = time.time()
    graph = readFile()
    parser = argparse.ArgumentParser()
    parser.add_argument("algorithm")
    parser.add_argument("source", type=int)
    parser.add_argument("destination", type=int)
    args =parser.parse_args()

    if args.algorithm == "D":
        result = Dijkstra(graph[0], args.source, args.destination)
        algorithm = "Dijkstra"
    elif args.algorithm == "B":
        result = BellmanFord(graph[0], args.source, args.destination)
        algorithm = "BellmanFord"
    else:
        usage()
    while 1:
        shortestpath.append(args.destination)
        if args.destination == args.source: break
        args.destination = result[1][args.destination]
    shortestpath.reverse()

    print "The distance from node %d to node %d using %s algorithm is %f" % (args.source, args.destination, algorithm, result[0])
    print "The execution time takes %s seconds." % (time.time() - starttime)
    print "The shortest path from node %d to node %d is: " % (args.source, args.destination),
    for i in shortestpath:
        print "%d, " % i,      