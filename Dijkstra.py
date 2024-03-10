import Distance


# Vertex class used to map delivery route on graph
class Vertex:
    # Vertices begin with a distance of infinity and no predecessor vertices
    def __init__(self, label):
        self.label = label
        self.distance = float('infinity')
        self.predecessor = None


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
    def addDirectedEdge(self, startVertex, endVertex, edgeWeight):
        self.edgeWeights[(startVertex, endVertex)] = edgeWeight
        self.adjacencyList[startVertex].append(endVertex)

    # Method creates 'undirected' edge by creating 2-way directed edge for each vertex
    def addUndirectedEdge(self, vertexC, vertexD, edgeWeight = 1.0):
        self.addDirectedEdge(vertexC, vertexD, edgeWeight)
        self.addDirectedEdge(vertexD, vertexC, edgeWeight)

    def printAdjacencyList(self, distance):
        for start, end in self.edgeWeights:
            print("START:", start.label, "END:", end.label, self.edgeWeights[(start, end)])

# Dijkstra algorithm implementation for delivery route
def dijkstraDeliveryRoute(graph, startVertex):
    # Begin by putting all vertices in a queue of unvisited vertices
    unvisitedQueue = []

    for currVertex in graph.adjacencyList:
        unvisitedQueue.append(currVertex)

    # Start vertex has a distance of 0 from itself
    startVertex.distance = 0

    # Vertices are visited individually until the list is empty
    while len(unvisitedQueue) > 0:
        # Assume index 0 has the shortest distance
        minDistanceIndex = 0

        # Find if any shorter distance vertex exists and update the minimum
        for i in range(1, len(unvisitedQueue)):
            if unvisitedQueue[i].distance < unvisitedQueue[minDistanceIndex].distance:
                minDistanceIndex = i

        # Visit the vertex with the shortest distance
        currVertex = unvisitedQueue.pop(minDistanceIndex)

        # Check each path length from current vertex to all neighboring vertices
        for adjacentVertex in graph.adjacencyList[currVertex]:
            # Pull the edge weight from dictionary using key:value pair
            #
            edgeWeight = graph.edgeWeights[(currVertex, adjacentVertex)]
            altPathDistance = currVertex.distance + edgeWeight

            # Compare alternate path of currentVertex-->adjacentVertex to startVertex-->adjacentVertex
            # If this alternate path is found to be shorter, update the adjacent vertex's distance and predecessor node
            if altPathDistance < adjacentVertex.distance:
                adjacentVertex.distance = altPathDistance
                adjacentVertex.predecessor = currVertex


def computeShortestPath(startVertex, endVertex, packageHashTable):
    shortestPath = ""
    currVertex = endVertex

    # i = 0
    while currVertex is not startVertex:
        # print("Loop: " + str(i))
        package = packageHashTable.search(currVertex.label)
        string = (" --> " + str(package.packageId))
        shortestPath = string + shortestPath
        currVertex = currVertex.predecessor
        # i += 1

    shortestPath = startVertex.label + shortestPath
    return shortestPath