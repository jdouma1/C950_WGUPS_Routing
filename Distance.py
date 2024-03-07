import csv
from Dijkstra import Vertex, Graph


class Distance:
    def __init__(self):
        self.distanceDataList = []
        self.addressDataList = [
"Western Governors University",
"1060 Dalton Ave S (84104)",
"1330 2100 S (84106)",
"1488 4800 S (84123)",
"177 W Price Ave (84115)",
"195 W Oakland Ave (84115)",
"2010 W 500 S (84104)",
"2300 Parkway Blvd (84119)",
"233 Canyon Rd (84103)",
"2530 S 500 E (84106)",
"2600 Taylorsville Blvd (84118)",
"2835 Main St (84115)",
"300 State St (84103)",
"3060 Lester St (84119)",
"3148 S 1100 W (84119)",
"3365 S 900 W (84119)",
"3575 W Valley Central Station bus Loop (84119)",
"3595 Main St (84115)",
"380 W 2880 S (84115)",
"410 S State St (84111)",
"4300 S 1300 E (84117)",
"4580 S 2300 E (84117)",
"5025 State St (84107)",
"5100 South 2700 West (84118)",
"5383 S 900 East #104 (84117)",
"600 E 900 South (84105)",
"6351 South 900 East (84121)"
]

        for i in range(len(self.addressDataList)):
            self.distanceDataList.append([])

# Method takes file and reads through entries to load distances into list[][]
def loadDistanceData(fileName, distanceDataList):
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
            distanceDataList[k] = rowDistances
            rowDistances = []
            k += 1

def loadTruckDeliveryGraph(distanceDataList, addressDataList):
    graph = Graph()

    '''
    Store each created vertex in list to eliminate key errors
    present when accessing adjacencyList dictionary in Dijkstra.py
    '''
    vertexList = []
    for address in addressDataList:
        vertex = Vertex(address)
        vertexList.append(vertex)

        graph.addVertex(vertex)

    j = 0
    for distanceList in distanceDataList:
        k = 0
        for distance in distanceList:
            startVertex = vertexList[j]
            endVertex = vertexList[k]
            # print(startVertex.label + " --> " + endVertex.label + " :: " + distance)
            graph.addDirectedEdge(startVertex, endVertex, float(distance))
            k += 1
        j += 1

    return graph
