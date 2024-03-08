class Truck:
    def __init__(self):
        self.truckPackages = []

    def loadPackage(self, package):
        self.truckPackages.append(package)

def loadTruckOnePackages(truck):
    # TRUCK 1
    # Must be delivered together and by specified time
    truck.loadPackage(13)  # 10:30 A.M.
    truck.loadPackage(14)  # 10:30 A.M.
    truck.loadPackage(15)  # 9:00 A.M.
    truck.loadPackage(16)  # 10:30 A.M.
    truck.loadPackage(19)  # EOD
    truck.loadPackage(20)  # 10:30 A.M.

    # Must be delivered by specified time
    truck.loadPackage(1)  # 10:30 A.M.
    truck.loadPackage(29)  # 10:30 A.M.
    truck.loadPackage(30)  # 10:30 A.M.
    truck.loadPackage(31)  # 10:30 A.M.

def loadTruckTwoPackages(truck):
    # TRUCK 2
    # Must be delivered by specified time
    truck.loadPackage(34)  # 10:30 A.M.
    truck.loadPackage(37)  # 10:30 A.M.
    truck.loadPackage(40)  # 10:30 A.M.

    # Can only be on truck 2
    truck.loadPackage(3)  # EOD
    truck.loadPackage(18)  # EOD
    truck.loadPackage(36)  # EOD
    truck.loadPackage(38)  # EOD

    truck.loadPackage(2)  # EOD
    truck.loadPackage(4)  # EOD
    truck.loadPackage(5)  # EOD
    truck.loadPackage(7)  # EOD
    truck.loadPackage(8)  # EOD

    '''
    END OF FIRST ROUND DELIVERIES
    '''

def reloadTruckOnePackages(truck):
    # TRUCK 1
    # Delayed flight, will not arrive at depot until 9:05 A.M.
    truck.loadPackage(6)  # 10:30 A.M.
    truck.loadPackage(25)  # 10:30 A.M.
    truck.loadPackage(28)  # EOD
    truck.loadPackage(32)  # EOD

    truck.loadPackage(35)  # EOD
    truck.loadPackage(39)  # EOD
    truck.loadPackage(10)  # EOD
    truck.loadPackage(11)  # EOD
    truck.loadPackage(12)  # EOD

def reloadTruckTwoPackages(truck):
    # TRUCK 2
    truck.loadPackage(17)  # EOD
    truck.loadPackage(21)  # EOD
    truck.loadPackage(22)  # EOD
    truck.loadPackage(23)  # EOD
    truck.loadPackage(24)  # EOD
    truck.loadPackage(26)  # EOD
    truck.loadPackage(27)  # EOD
    truck.loadPackage(33)  # EOD

    # Correct address unknown until 10:20 A.M.
    truck.loadPackage(9)  # EOD