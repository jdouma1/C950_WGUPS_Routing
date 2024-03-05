#Class used for creating packages and package data for hash table
class Package:
    # Constructor for package to store address and other key information
    def __init__(self, packageId, address, city, state, zipCode, deliveryDeadline, edgeWeight):
        self.packageId = packageId
        self.address = address
        self.city = city
        self.state = state
        self.zipCode = zipCode
        self.deliveryDeadline = deliveryDeadline
        self.edgeWeight = edgeWeight

    # Method to overwrite how package is printed to print data instead of object
    def __str__(self):
        return "%s, %s, %s, %s, %s, %s, %s" % (self.packageId, self.address, self.city, self.state, self.zipCode, self.deliveryDeadline, self.edgeWeight)