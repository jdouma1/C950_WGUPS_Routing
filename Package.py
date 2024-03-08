import csv


# Class used for creating packages and package data for hash table
class Package:
    # Constructor for package to store address and other key information
    def __init__(self, packageId, address, city, state, zipCode, deliveryDeadline, weight):
        self.packageId = packageId
        self.address = address
        self.city = city
        self.state = state
        self.zipCode = zipCode
        self.deliveryDeadline = deliveryDeadline
        self.weight = weight

    # Method to overwrite how package is printed to print data instead of object
    def __str__(self):
        return "%s, %s, %s, %s, %s, %s, %s" % (self.packageId, self.address, self.city, self.state, self.zipCode, self.deliveryDeadline, self.weight)

    # Method takes file and reads through entries to load packages into hash table
def loadPackageData(fileName, packageHashTable):
    with open(fileName) as packages:
        packageData = csv.reader(packages, delimiter=',')
        next(packageData)  # Skip the header
        for package in packageData:
            packageId = int(package[0])
            address = package[1]
            city = package[2]
            state = package[3]
            zipCode = int(package[4])
            deliveryDeadline = package[5]
            weight = int(package[6])

            # Create and insert new package into hash table
            newPackage = Package(packageId, address, city, state, zipCode, deliveryDeadline, weight)
            address = address.replace('"', '')
            address = address + " " + str(zipCode)
            address = address.strip()
            print(address)
            packageHashTable.insert(address, newPackage)
