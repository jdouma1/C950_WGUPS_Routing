import csv
from Dijkstra import Vertex, Graph


# Distance class used to read and store distance table and vertex data from CSV files
class Distance:
    # Constructor initializes address data and declares distanceTable and vertexList
    def __init__(self):
        # Stores list of vertices for consistency when referencing adjacencyList dictionary
        self.vertexList = []
        self.distanceTable = []
        for i in range(27):
            self.distanceTable.append([])
        # Size 27
        self.addressDataList = [
            "Western Governors University",
            "1060 Dalton Ave S 84104",
            "1330 2100 S 84106",
            "1488 4800 S 84123",
            "177 W Price Ave 84115",
            "195 W Oakland Ave 84115",
            "2010 W 500 S 84104",
            "2300 Parkway Blvd 84119",
            "233 Canyon Rd 84103",
            "2530 S 500 E 84106",
            "2600 Taylorsville Blvd 84118",
            "2835 Main St 84115",
            "300 State St 84103",
            "3060 Lester St 84119",
            "3148 S 1100 W 84119",
            "3365 S 900 W 84119",
            "3575 W Valley Central Station bus Loop 84119",
            "3595 Main St 84115",
            "380 W 2880 S 84115",
            "410 S State St 84111",
            "4300 S 1300 E 84117",
            "4580 S 2300 E 84117",
            "5025 State St 84107",
            "5100 South 2700 West 84118",
            "5383 S 900 East #104 84117",
            "600 E 900 South 84105",
            "6351 South 900 East 84121"
        ]
        '''
        self.addressKeyList = [
            "Western Governors University",
            "106084104",
            "133084106",
            "148884123",
            "17784115",
            "19584115",
            "201084104",
            "230084119",
            "23384103",
            "253084106",
            "260084118",
            "283584115",
            "30084103",
            "306084119",
            "314884119",
            "336584119",
            "357584119",
            "359584115",
            "38084115",
            "41084111",
            "430084117",
            "458084117",
            "502584107",
            "510084118",
            "538384117",
            "60084105",
            "635184121"
        ]
        '''


# Method takes file and reads through entries to load distances into table
def loadDistanceData(fileName, distanceTable):
    with open(fileName) as distances:
        distanceData = csv.reader(distances, delimiter=' ')
        next(distanceData)  # Skip the header
        rowDistances = []
        # Index tracks which row of distanceDataList 2D array
        k = 0
        for distance in distanceData:
            for j in range(len(distance)):
                rowDistances.append(distance[j])
            # Replace empty row with list of row distances then reset rowDistances
            distanceTable[k] = rowDistances
            rowDistances = []
            k += 1


# Method loads vertices and edges into graph
def loadGraph(distanceObject):
    # Store each created vertex in list for later reference to eliminate key errors
    # present when accessing adjacencyList dictionary in Dijkstra.py.
    # Errors are present due to variability in hash values when creating new vertex.
    graph = Graph()
    vertexList = []
    for address in distanceObject.addressDataList:
        vertex = Vertex(address)
        vertexList.append(vertex)
        graph.addVertex(vertex)
    distanceObject.vertexList = vertexList

    j = 0
    for distanceList in distanceObject.distanceTable:
        k = 0
        for distance in distanceList:
            startVertex = vertexList[j]
            endVertex = vertexList[k]
            graph.addUndirectedEdge(startVertex, endVertex, float(distance))
            k += 1
        j += 1
    return graph
