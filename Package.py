import csv
import datetime

import Truck


# Class used for creating packages and package data for hash table
class Package:
    # Constructor for package to store address and other key information
    def __init__(self, packageId, address, city, state, zipCode, deliveryDeadline, weight, deliveryStatus, truckNumber="", truck=None):
        self.packageId = packageId
        self.address = address
        self.city = city
        self.state = state
        self.zipCode = zipCode
        self.deliveryDeadline = deliveryDeadline
        self.weight = weight
        # These three keep truck of delivery time and by which truck
        self.deliveryStatus = deliveryStatus
        self.truckNumber = truckNumber
        self.truck = truck

    # Method to overwrite how package is printed to print data instead of object
    # Time may be specified to view package's status at that instance (truck is to be specified alongside time)
    def __str__(self, requestedTime=None):
        # Return normal package information including when it was delivered
        if requestedTime is None:
            return "%s, %s, %s, %s, %s, %s, %s, Delivered by truck %s at: %s" % (self.packageId, self.address, self.city, self.state, self.zipCode, self.deliveryDeadline, self.weight, self.truckNumber, self.deliveryStatus)

        deliveryTime = Truck.getTimeDecimal(self.deliveryStatus)
        # Package has been delivered already
        if deliveryTime <= requestedTime:
            return "%s, %s, %s, %s, %s, %s, %s, Delivered by truck %s at: %s" % (self.packageId, self.address, self.city, self.state, self.zipCode, self.deliveryDeadline, self.weight, self.truckNumber, self.deliveryStatus)
        # Package has left the hub already
        else:
            secondRoundStart = Truck.getTimeDecimal(self.truck.secondRoundStart)
            # Package was delivered in the first round
            if secondRoundStart > Truck.getTimeDecimal(self.deliveryStatus):
                departureTime = Truck.getTimeDecimal(datetime.timedelta(hours=int(8), minutes=int(0), seconds=int(0)))
                if departureTime <= requestedTime:
                    return "%s, %s, %s, %s, %s, %s, %s, En Route by truck %s since: %s" % (self.packageId, self.address, self.city, self.state, self.zipCode, self.deliveryDeadline, self.weight, self.truckNumber, departureTime)
            # Package was delivered in the second round
            else:
                if secondRoundStart <= requestedTime:
                    return "%s, %s, %s, %s, %s, %s, %s, En Route by truck %s since: %s" % (self.packageId, self.address, self.city, self.state, self.zipCode, self.deliveryDeadline, self.weight, self.truckNumber, secondRoundStart)
            # Package is still at the hub
            return "%s, %s, %s, %s, %s, %s, %s, At Hub" % (self.packageId, self.address, self.city, self.state, self.zipCode, self.deliveryDeadline, self.weight)



# Method takes file and reads through entries to load packages into hash table
def loadPackageData(fileName, packageHashTable):
    with open(fileName) as packages:
        packageData = csv.reader(packages, delimiter=',')
        next(packageData)  # Skip the header
        for package in packageData:
            packageId = int(package[0])
            address = (package[1].replace('"', '')).strip()
            city = package[2]
            state = package[3]
            zipCode = int(package[4])
            deliveryDeadline = package[5]
            weight = int(package[6])
            deliveryStatus = "At Hub"

            # Create and insert new package into hash table
            newPackage = Package(packageId, address, city, state, zipCode, deliveryDeadline, weight, deliveryStatus)
            packageHashTable.insert(packageId, newPackage)
