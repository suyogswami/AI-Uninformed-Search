################################################################################
##  Name: Suyog Swami
##  Subject: CSE5360: Artificial Intelligence I
##  Assignment: Uninformed Search
##  Students ID: 1001119101
################################################################################

import sys

source_path = {}
source_distance = {}

class Graph(object):
    node_dictionary = dict
    edge_attr_dictionary = dict
    adjlist_dictionary = dict

# Constructor for Graph()
    def __init__(self, data=None, **ptr):
        nd = self.node_dictionary
        self.node = nd()
        self.adjacent = nd()
        self.graph = {}

# add node
    def addnode(self, n, dicti=None, **ptr):
        if dicti is None:
            dicti = ptr
        else:
            try:
                dicti.update(ptr)
            except Exception:
				print 'Error in adding node'
        if n in self.node:
            self.node[n].update(dicti)
        else:
            self.adjacent[n] = self.adjlist_dictionary()
            self.node[n] = dicti

# add edge
    def addedge(self, m, n, dicti=None, **ptr):
        if dicti is None:
            dicti = ptr
        else:
            try:
                dicti.update(ptr)
            except AttributeError:
                print 'Error in adding edge'

        if m not in self.node:
            self.adjacent[m] = self.adjlist_dictionary()
            self.node[m] = {}
        if n not in self.node:
            self.adjacent[n] = self.adjlist_dictionary()
            self.node[n] = {}

        datadict = self.adjacent[m].get(n, self.edge_attr_dictionary())
        datadict.update(dicti)
        self.adjacent[m][n] = datadict
        self.adjacent[n][m] = datadict

# get nodes
    def getnodes(self, data=False):
        if data:
            return iter(self.node.items())
        return iter(self.node)

#get edge
    def getedge(self, u, v, default=None):
        try:
            return self.adjacent[u][v]
        except KeyError:
            return default

# get neighbors
    def getneighbors(self, n):
        try:
            return list(self.adjacent[n])
        except KeyError:
            print 'Error in getting neighbors'

def main(argv):
    # read argurments
    filename=argv[1]
    source=argv[2]
    desti=argv[3]

    # initiate Graph
    graph=Graph()
    # open and read file
    file_data=open(filename)
    for data in file_data:
        if data.strip()=="END OF INPUT":
            break
        line_data=data.split()
        weight=int(line_data[2])

        #create graph
        # add nodes and edges
        graph.addnode(line_data[0])
        graph.addnode(line_data[1])
        graph.addedge(line_data[0],line_data[1],dist=weight)

    # initiate source with distance 0 else infinity
    for node in graph.getnodes():
        if node == source:
            source_distance[node] = 0
            source_path[node] = [node]
        else:
            source_distance[node] = float('inf')
            source_path[node] = []

    nlist = []
    nlist.append((0,source))
    nlist = sorted(nlist, key=lambda col: col[0])

    # search for neighbors with shortest edge
    while len(nlist):
        next_node= nlist.pop(0)
        neighborslist = graph.getneighbors(next_node[1])
        for n in neighborslist:
            edge_n=graph.getedge(next_node[1],n)['dist']
            d = next_node[0] + edge_n
            if d < source_distance[n]:
                p = source_path[next_node[1]] + [n]
                source_distance[n] = d
                source_path[n] = p
                nlist.append((d,n))
                nlist = sorted(nlist, key=lambda col: col[0])

    # find the shortest path
    if source_distance[desti] < float('inf'):
        pathlist = source_path[desti]
        print 'distance: ' + str(source_distance[desti]) + ' km'
        print 'route:'
        for i in range(1,len(pathlist)):
            p=pathlist[i-1]
            q=pathlist[i]
            edge_p_q=graph.getedge(pathlist[i-1],pathlist[i])['dist']
            print '%s to %s, %s km' %(p,q,edge_p_q)
    else:
        print 'distance: infinity'
        print 'route:'
        print 'none'

if __name__ == '__main__':
    main(sys.argv)