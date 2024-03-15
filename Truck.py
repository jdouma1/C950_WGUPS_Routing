# Truck class used to manually/heuristically load packages for delivery by Dijkstra
class Truck:
    # Constructor initializes empty list to store packages for delivery
    def __init__(self):
        self.truckPackages = []
        self.distanceTraveled = 0

    # Method loads list of packages provided
    def loadPackages(self, packageList):
        for package in packageList:
            self.truckPackages.append(package)

    # Greedy method to delivery packages based on nearest vertex from current
    def unloadPackages(self, graph, distance, currentTime, hashTable):
        # Initialize lists of distances between vertices, the vertices and packages themselves
        # The first vertex appended is the hub, WGU
        avgSpeed = 18.00  # Mph
        timeHrs = 8.00  # In Hours
        listDistances = []
        listVertices = []
        listPackages = []
        # List used to store vertices based off nearest neighbor distance for delivery order
        verticesInDeliveryOrder = []
        # Stores distances in delivery order to calculate time
        distancesInDeliveryOrder = []
        # Save Hub location for beginning and end of delivery distance and time calculation
        hubVertex = distance.vertexList[0]
        finalVertex = None

        # Search the hashtable for each package and append each package to list
        for id in self.truckPackages:
            package = hashTable.search(id)
            listPackages.append(package)
            # Search for corresponding vertex and append to list
            vertex = distance.getVertex(package)
            listVertices.append(vertex)

        # Start from Hub and find nearest neighbor to deliver to, appending result to verticesInDeliveryOrder
        currVertex = hubVertex
        j = 0
        while j < len(listPackages):
            # Current vertex becomes chosen nearest neighbor upon each new iteration of while loop
            for i in range(len(listVertices)):
                listDistances.append(graph.edgeWeights[(currVertex, listVertices[i])])
            minDistance = min(listDistances)
            minIndex = listDistances.index(minDistance)
            currVertex = listVertices[minIndex]
            verticesInDeliveryOrder.append(currVertex)
            distancesInDeliveryOrder.append(minDistance)
            # Remove vertex from list since it has already been visited
            listVertices.pop(minIndex)
            # Reset list of distances for new current vertex
            listDistances = []
            j += 1

        # Since packages may share address, use boolean to determine if a delivery has been made
        continueSearch = True
        finalVertex = verticesInDeliveryOrder[(len(verticesInDeliveryOrder) - 1)]
        for j in range(len(verticesInDeliveryOrder)):
            k = 0
            while k < len(listPackages):
                vertex = distance.getVertex(listPackages[k])
                if vertex.label == verticesInDeliveryOrder[j].label and continueSearch is True:
                    timeHrsBetweenVertices = round((distancesInDeliveryOrder[j] / avgSpeed), 2)
                    timeHrs = round((timeHrs + timeHrsBetweenVertices), 2)
                    print("Delivered package " + str(listPackages[k].packageId) + " to " + vertex.label + " at " + str(timeHrs))
                    listPackages.pop(k)
                    # Decrement index since list has shortened
                    k -= 1
                    continueSearch = False
                k += 1
            continueSearch = True
        finalDistance = graph.edgeWeights[(finalVertex, hubVertex)]
        timeHrsBetweenVertices = round((finalDistance / avgSpeed), 2)
        timeHrs = round((timeHrs + timeHrsBetweenVertices), 2)
        print("Returned to hub at " + str(timeHrs))
        print()
        print()
        return currentTime


def loadTruckOnePackages(truck):
    # TRUCK 1
    # Must be delivered together and by specified time
    # [13, 14, 16, 20]: 10:30 A.M. // [15]: 9:00 A.M. // [19]: EOD
    truck.loadPackages([13, 14, 15, 16, 19, 20])

    # Must be delivered by specified time (10:30 A.M.)
    truck.loadPackages([1, 29, 30, 31])  # 10:30 A.M.


def loadTruckTwoPackages(truck):
    # TRUCK 2
    # Must be delivered by specified time (10:30 A.M.)
    truck.loadPackages([34, 37, 40])

    # Can only be on truck 2 (EOD)
    truck.loadPackages([3, 18, 36, 38])

    # Extra packages to be loaded (EOD)
    truck.loadPackages([2, 4, 5, 7, 8])

# *****
# END OF FIRST ROUND DELIVERIES
# *****


def reloadTruckOnePackages(truck):
    # TRUCK 1
    # Delayed flight, will not arrive at depot until 9:05 A.M.
    # [6, 25]: 10:30 A.M. // [28, 32]: EOD
    truck.loadPackages([6, 25, 28, 32])

    # Extra packages to be loaded (EOD)
    truck.loadPackages([35, 39, 10, 11, 12])


def reloadTruckTwoPackages(truck):
    # TRUCK 2 (EOD)
    truck.loadPackages([17, 21, 22, 23, 24, 26, 27, 33])

    # Correct address unknown until 10:20 A.M. (EOD)
    truck.loadPackages([9])
