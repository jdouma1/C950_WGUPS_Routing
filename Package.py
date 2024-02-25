class Package:
    def __init__(self, packageId, address, city, state, zipCode, deliveryDeadline, weight):
        self.packageId = packageId
        self.address = address
        self.city = city
        self.state = state
        self.zipCode = zipCode
        self.deliveryDeadline = deliveryDeadline
        self.weight = weight

    def __str__(self):
        return "%s, %s, %s, %s, %s, %s, %s" % (self.packageId, self.address, self.city, self.state, self.zipCode, self.deliveryDeadline, self.weight)