# Jacob Douma / Student ID: 010764471

import datetime
from HashTable import HashTable
from Package import loadPackageData
from Distance import Distance, loadDistanceData, loadGraph
from Dijkstra import dijkstraDeliveryRoute, computeShortestPath
from Truck import Truck, loadTruckOnePackages, reloadTruckOnePackages, loadTruckTwoPackages, reloadTruckTwoPackages

# Global variable for hash table, distance table data, and current time for deliveries
# 8:00 A.M. is when trucks depart the depot for delivery
packageHashTable = HashTable()
distance = Distance()
currentTime = datetime.timedelta(hours=int(8), minutes=int(0), seconds=int(0))


if __name__ == '__main__':
    # Load packages into hash table from csv file
    loadPackageData("Packages.csv", packageHashTable)

    # Load distance and address data into lists from csv file
    loadDistanceData("Distances.csv", distance.distanceTable)

    # Initialize graph with edges present in distance table
    graph = loadGraph(distance)

    # Perform Dijkstra to find the shortest routes between vertices on graph
    dijkstraDeliveryRoute(graph, distance.vertexList[0])

    truck1 = Truck()
    truck2 = Truck()

    # Load first round packages
    loadTruckOnePackages(truck1)
    loadTruckTwoPackages(truck2)
    # Deliver first round packages
    # verticesList = computeShortestPath(distance.vertexList[12], distance.vertexList[0], packageHashTable)
    truck1.unloadPackages(graph, distance, currentTime, packageHashTable)

    # Load next round packages
    reloadTruckOnePackages(truck1)
    reloadTruckTwoPackages(truck2)
    # Deliver next round packages (CODE MISSING)



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
