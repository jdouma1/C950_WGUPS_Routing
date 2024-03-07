# Jacob Douma / Student ID: 010764471

from HashTable import HashTable
from Package import loadPackageData
from Distance import Distance, loadDistanceData, loadTruckDeliveryGraph
from Dijkstra import Vertex, Graph, dijkstraDeliveryRoute, computeShortestPath

# Global variable for hash table
packageHashTable = HashTable()
distance = Distance()


if __name__ == '__main__':
    # Load packages into hash table from csv file
    loadPackageData("Packages.csv", packageHashTable)

    # Load distance and address data into lists from csv file
    loadDistanceData("Distances.csv", distance.distanceDataList)

    # Initialize graph with edges present in distance table
    graph = loadTruckDeliveryGraph(distance.distanceDataList, distance.addressDataList)

    # Iterate over packages in hash table and print data
    # for i in range(len(packageHashTable.table) + 1):
        # print("Key:", str(i+1), " and Package: ", packageHashTable.search(i+1))

    # print()
    # print()
    # print()
    # for i in range(len(distance.distanceDataList)):
        # print(distance.distanceDataList[i])
    #print(distance.distanceDataList[1])
