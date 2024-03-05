#import csv
from HashTable import HashTable
from Package import loadPackageData
from Dijkstra import Vertex, Graph, dijkstraDeliveryRoute

# Global variable for hash table
packageHashTable = HashTable()

'''
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
'''

if __name__ == '__main__':
    # Load packages into hash table from csv file
    loadPackageData("Packages.csv", packageHashTable)

    # Iterate over packages in hash table and print data
    for i in range(len(packageHashTable.table) + 1):
        print("Key:", str(i+1), " and Package: ", packageHashTable.search(i+1))

