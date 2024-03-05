import csv
from HashTable import HashTable
from Package import Package

# Global variable for hash table
packageHashTable = HashTable()


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

# Method takes file and reads through entries to load packages into hash table
def loadPackageData(fileName):
    with open(fileName) as packages:
        packageData = csv.reader(packages, delimiter=',')
        next(packageData) # Skip the header
        for package in packageData:
            packageId = int(package[0])
            address = package[1]
            city = package[2]
            state = package[3]
            zipCode = int(package[4])
            deliveryDeadline = package[5]
            edgeWeight = int(package[6])

            # Create and insert new package into hash table
            newPackage = Package(packageId, address, city, state, zipCode, deliveryDeadline, edgeWeight)
            packageHashTable.insert(packageId, newPackage)


if __name__ == '__main__':
    # Load packages into hash table from csv file
    loadPackageData("Packages.csv")

    # Iterate over packages in hash table and print data
    for i in range(len(packageHashTable.table) + 1):
        print("Key:", str(i+1), " and Package: ", packageHashTable.search(i+1))

