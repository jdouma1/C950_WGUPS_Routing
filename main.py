# Jacob Douma / Student ID: 010764471
import datetime
from HashTable import HashTable
from Package import loadPackageData
from Distance import Distance, loadDistanceData, loadGraph
from Dijkstra import Vertex, Graph, dijkstraDeliveryRoute, computeShortestPath
from Truck import Truck, loadTruckOnePackages, reloadTruckOnePackages, loadTruckTwoPackages, reloadTruckTwoPackages

# Global variable for hash table, distance table data, and current time for deliveries
packageHashTable = HashTable()
distance = Distance()
currentTime = datetime.timedelta(hours=int(8), minutes=int(0), seconds=int(0))


if __name__ == '__main__':
    # Load packages into hash table from csv file
    loadPackageData("Packages.csv", packageHashTable)
    for i in range(len(packageHashTable.table) + 1):
        print("Key:", str(i + 1), "and Package:", packageHashTable.search(distance.addressDataList[i]))

    # Load distance and address data into lists from csv file
    loadDistanceData("Distances.csv", distance.distanceDataList)

    # Initialize graph with edges present in distance table
    graph = loadGraph(distance)
    dijkstraDeliveryRoute(graph, distance.vertexList[0])

    truck1 = Truck()
    truck2 = Truck()

    # Load first round packages
    loadTruckOnePackages(truck1)
    loadTruckTwoPackages(truck2)
    # Deliver first round packages

    # Load next round packages
    reloadTruckOnePackages(truck1)
    reloadTruckTwoPackages(truck2)
    # Deliver next round packages

    print(computeShortestPath(distance.vertexList[0], distance.vertexList[16], packageHashTable))
    '''
    loop = True
    while loop is True:
        print("OPTIONS:")
        print("1: Print All Package Status and Total Mileage ")
        print("2: Get a Single Package Status with a Time")
        print("3: Get All Package Status with a Time")
        print("4: Exit the Program")

        choice = input()
        if choice == '1':
            print('1')
        if choice == '2':
            print('2')
        if choice == '3':
            print('3')
        if choice == '4':
            loop = False
            break
    '''


    '''
    Iterate over packages in hash table and print data
    for i in range(len(packageHashTable.table) + 1):
        print("Key:", str(i+1), " and Package: ", packageHashTable.search(i+1))

    print()
    print()
    print()
    for i in range(len(distance.distanceDataList)):
        print(distance.distanceDataList[i])
    print(distance.distanceDataList[1])
    '''
