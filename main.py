# Jacob Douma / Student ID: 010764471

import datetime

import Package
from HashTable import HashTable
from Package import loadPackageData
from Distance import Distance, loadDistanceData, loadGraph
from Truck import Truck, loadTruckOnePackages, reloadTruckOnePackages, loadTruckTwoPackages, reloadTruckTwoPackages, getTimeDecimal, getTimeDelta

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

    # Create trucks 1 and 2 to be loaded for delivery
    truck1 = Truck(1)
    truck2 = Truck(2)
    currentTimeTruck1 = currentTime
    currentTimeTruck2 = currentTime

    # Load first round packages
    loadTruckOnePackages(truck1)
    loadTruckTwoPackages(truck2)

    # Deliver first round packages
    currentTimeTruck1 = truck1.nearestNeighborUnloadPackages(graph, distance, packageHashTable, currentTimeTruck1)
    currentTimeTruck2 = truck2.nearestNeighborUnloadPackages(graph, distance, packageHashTable, currentTimeTruck2)

    # Load next round packages
    reloadTruckOnePackages(truck1)
    reloadTruckTwoPackages(truck2)
    # Deliver next round packages
    currentTimeTruck1 = truck1.nearestNeighborUnloadPackages(graph, distance, packageHashTable, currentTimeTruck1)
    currentTimeTruck2 = truck2.nearestNeighborUnloadPackages(graph, distance, packageHashTable, currentTimeTruck2)

    loop = True
    while loop is True:
        print("OPTIONS:")
        print("1: Print All Package Status and Total Mileage")
        print("2: Get a Single Package Status with a Time")
        print("3: Get All Package Status with a Time")
        print("4: Exit the Program\n")

        choice = input()
        if choice == '1':
            packageHashTable.printAllPackages()
            print("\nTotal miles traveled: " + str(truck1.getTotalDistanceTraveled() + truck2.getTotalDistanceTraveled()) + "\n")
        if choice == '2':
            packageId = int(input("Enter the package you would like to view: "))
            print()
            print("Enter the time you would like to view its status: ")
            hours = int(input("Hours: "))
            minutes = int(input("Minutes: "))
            timedelta = datetime.timedelta(hours=int(hours), minutes=int(minutes), seconds=int(0))
            timeDecimal = getTimeDecimal(timedelta)
            packageHashTable.printPackage(packageId, timeDecimal)
            print()
        if choice == '3':
            print("Enter the time you would like to view the packages: ")
            hours = int(input("Hours: "))
            minutes = int(input("Minutes: "))
            timedelta = datetime.timedelta(hours=int(hours), minutes=int(minutes), seconds=int(0))
            timeDecimal = getTimeDecimal(timedelta)
            packageHashTable.printAllPackages(timeDecimal)
        if choice == '4':
            loop = False
            break
