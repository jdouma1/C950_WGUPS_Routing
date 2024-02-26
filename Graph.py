# Class used for mapping vertices onto a graph
class Graph:
    # Adjacency list stores key:value of vertices and their edges with other vertices
    # Edge weights stores key:value of vertices and the weight of their edges with other vertices
    def __init__(self):
        self.adjacencyList = {}
        self.edgeWeights = {}

    # Method adds a new key for new vertex with empty adjacency list
    def addVertex(self, vertex):
        self.adjacencyList[vertex] = []

    # Method updates values for edge weight and adjacency list for start and end vertex
    def addDirectedEdge(self, startVertex, endVertex, weight):
        self.edgeWeights[(startVertex, endVertex)] = weight
        self.adjacencyList[startVertex].append(endVertex)

    # Method creates 'undirected' edge by creating 2-way directed edge for each vertex
    def addUndirectedEdge(self, vertexC, vertexD, weight = 1.0):
        self.addDirectedEdge(vertexC, vertexD, weight)
        self.addDirectedEdge(vertexD, vertexC, weight)