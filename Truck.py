# Truck class used to manually/heuristically load packages for delivery by Dijkstra
import datetime


class Truck:
    # Constructor initializes empty list to store packages for delivery
    def __init__(self, truckNumber):
        self.truckNumber = truckNumber
        self.firstRoundPackages = []
        self.secondRoundPackages = []
        self.secondRoundStart = 0
        self.distanceTraveled = 0
        self.round = 1

    # Method returns either packages loaded on first round or second round of deliveries
    def getTruckPackages(self):
        if self.round == 1:
            return self.firstRoundPackages
        if self.round == 2:
            return self.secondRoundPackages

    # Method returns the total distance the truck has traveled in miles
    def getTotalDistanceTraveled(self):
        return self.distanceTraveled

    # Method loads list of packages provided
    def loadPackages(self, packageList):
        for package in packageList:
            if self.round == 1:
                self.firstRoundPackages.append(package)
            if self.round == 2:
                self.secondRoundPackages.append(package)

    # Greedy method to delivery packages based on nearest vertex from current
    def nearestNeighborUnloadPackages(self, graph, distance, hashTable, currentTime):
        if self.round == 2:
            self.secondRoundStart = currentTime
            startDecimal = getTimeDecimal(self.secondRoundStart)
            if startDecimal >= 10.2:
                package = hashTable.search(9)
                package.address = "410 S State St"
                package.city = "Salt Lake City"
                package.state = "UT"
                package.zipCode = 84111
                hashTable.insert(9, package)
        # Initialize lists of distances between vertices, the vertices and packages themselves
        # The first vertex appended is the hub, WGU
        avgSpeed = 18.00  # Mph
        timeHrs = getTimeDecimal(currentTime)  # In Hours
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
        truckPackages = self.getTruckPackages()
        for id in truckPackages:
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
            # Find the shortest distance in list of neighboring vertices
            minDistance = min(listDistances)
            # Find the index in the list where the shortest distance is, and pull the vertex from that index
            minIndex = listDistances.index(minDistance)
            currVertex = listVertices[minIndex]
            # The vertex with the shortest distance becomes the next vertex in order to deliver to
            verticesInDeliveryOrder.append(currVertex)
            distancesInDeliveryOrder.append(minDistance)
            # Remove vertex from list since it has already been visited
            listVertices.pop(minIndex)
            # Reset list of distances for new current vertex
            listDistances = []
            j += 1

        # Since packages may share address, use boolean to determine if a delivery has been made
        continueSearch = True
        # Stores the address of the final package to be delivered. Used to calculate distance between address and Hub
        finalVertex = verticesInDeliveryOrder[(len(verticesInDeliveryOrder) - 1)]
        for j in range(len(verticesInDeliveryOrder)):
            k = 0
            while k < len(listPackages):
                vertex = distance.getVertex(listPackages[k])
                # If addresses match and package has not already been delivered this iteration
                if vertex.label == verticesInDeliveryOrder[j].label and continueSearch is True:
                    # Updates total distance traveled by the truck
                    self.distanceTraveled += distancesInDeliveryOrder[j]
                    # Time to travel distance to next vertex rounded 2 decimal places
                    timeHrsBetweenVertices = round((distancesInDeliveryOrder[j] / avgSpeed), 2)
                    timeHrs = round((timeHrs + timeHrsBetweenVertices), 2)
                    print("Delivered package " + str(listPackages[k].packageId) + " to " + vertex.label + " at", end=" ")
                    # Update package delivery time and truck
                    package = listPackages[k]
                    package.deliveryStatus = getTimeDelta(timeHrs)
                    package.truckNumber = self.truckNumber
                    package.truck = self
                    hashTable.insert(package.packageId, package)
                    print(hashTable.search(package.packageId).deliveryStatus)
                    listPackages.pop(k)
                    # Decrement index since list has shortened
                    k -= 1
                    continueSearch = False
                k += 1
            continueSearch = True
        # Calculate distance and travel time between final delivery and Hub
        finalDistance = graph.edgeWeights[(finalVertex, hubVertex)]
        timeHrsBetweenVertices = round((finalDistance / avgSpeed), 2)
        timeHrs = round((timeHrs + timeHrsBetweenVertices), 2)
        print("Returned to hub at", end=" ")
        print(getTimeDelta(timeHrs))
        print()
        print()
        currentTime = getTimeDelta(timeHrs)
        return currentTime


def loadTruckOnePackages(truck):
    # TRUCK 1
    # [13, 14, 16, 20]: 10:30 A.M. // [15]: 9:00 A.M. // [19]: EOD
    # Must be delivered together and by specified time
    truck.loadPackages([13, 14, 15, 16, 19, 20])

    # Must be delivered by specified time (10:30 A.M.)
    truck.loadPackages([1, 31])  # 10:30 A.M.


def loadTruckTwoPackages(truck):
    # TRUCK 2
    # Must be delivered by specified time (10:30 A.M.)
    truck.loadPackages([29, 30, 34, 37, 40])

    # Can only be on truck 2 (EOD)
    truck.loadPackages([3, 18])

    # Extra packages to be loaded (EOD)
    truck.loadPackages([2, 17, 21, 22, 23, 24, 26, 27])

# *****
# END OF FIRST ROUND DELIVERIES
# *****


def reloadTruckOnePackages(truck):
    truck.round = 2
    truck.truckPackages = []
    # TRUCK 1
    # [6, 25]: 10:30 A.M. // [28, 32]: EOD
    # Delayed flight, will not arrive at depot until 9:05 A.M.
    truck.loadPackages([6, 25, 28, 32])

    # Extra packages to be loaded (EOD)
    truck.loadPackages([35, 39, 10, 11, 12])


def reloadTruckTwoPackages(truck):
    truck.round = 2
    truck.truckPackages = []
    # TRUCK 2
    # Extra packages to be loaded (EOD) // [36, 38] CAN ONLY BE ON TRUCK 2
    truck.loadPackages([4, 5, 7, 8, 33, 36, 38])

    # Correct address unknown until 10:20 A.M. (EOD)
    truck.loadPackages([9])


# Given decimal value of time in hours, return timeDelta of hours, minutes, seconds
def getTimeDelta(hoursDecimal):
    # Get hours and update decimal - hours
    hours = int(hoursDecimal)
    timeHrs = round((hoursDecimal - hours), 2)
    # print("Hours: " + str(hours))

    # Get minutes and update decimal - minutes
    timeHrs = round((timeHrs * 60), 2)
    minutes = int(timeHrs)
    # print("Minutes: " + str(minutes))

    # Get seconds and update decimal - seconds
    timeHrs = timeHrs - minutes
    seconds = int(timeHrs * 60)
    # print("Seconds: " + str(seconds))

    timedelta = datetime.timedelta(hours=hours, minutes=minutes, seconds=seconds)
    return timedelta


def getTimeDecimal(timedelta):
    totalSeconds = timedelta.total_seconds()
    hours = int(totalSeconds / 3600)
    totalSeconds = totalSeconds - (3600 * hours)
    minutes = int(totalSeconds / 60)
    totalSeconds = totalSeconds - (minutes * 60)
    seconds = totalSeconds

    timeDecimal = round((float(hours) + float(minutes / 60.0) + float(seconds / 3600.0)), 2)

    return timeDecimal
