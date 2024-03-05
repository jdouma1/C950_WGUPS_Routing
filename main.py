from HashTable import HashTable
from Package import loadPackageData
from Dijkstra import Vertex, Graph, dijkstraDeliveryRoute, computeShortestPath

# Global variable for hash table
packageHashTable = HashTable()


if __name__ == '__main__':
    # Load packages into hash table from csv file
    loadPackageData("Packages.csv", packageHashTable)

    # Iterate over packages in hash table and print data
    for i in range(len(packageHashTable.table) + 1):
        print("Key:", str(i+1), " and Package: ", packageHashTable.search(i+1))

