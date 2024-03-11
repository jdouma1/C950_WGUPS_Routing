# Truck class used to manually/heuristically load packages for delivery by Dijkstra
class Truck:
    # Constructor initializes empty list to store packages for delivery
    def __init__(self):
        self.truckPackages = []

    # Method loads list of packages provided
    def loadPackages(self, packageList):
        for package in packageList:
            self.truckPackages.append(package)


def loadTruckOnePackages(truck):
    # TRUCK 1
    # Must be delivered together and by specified time
    # [13, 14, 16, 20]: 10:30 A.M. // [15]: 9:00 A.M. // [19]: EOD
    truck.loadPackages([13, 14, 15, 16, 19, 20])

    # Must be delivered by specified time (10:30 A.M.)
    truck.loadPackages([1, 29, 30, 31])  # 10:30 A.M.


def loadTruckTwoPackages(truck):
    # TRUCK 2
    # Must be delivered by specified time (10:30 A.M.)
    truck.loadPackages([34, 37, 40])

    # Can only be on truck 2 (EOD)
    truck.loadPackages([3, 18, 36, 38])

    # Extra packages to be loaded (EOD)
    truck.loadPackages([2, 4, 5, 7, 8])

# *****
# END OF FIRST ROUND DELIVERIES
# *****


def reloadTruckOnePackages(truck):
    # TRUCK 1
    # Delayed flight, will not arrive at depot until 9:05 A.M.
    # [6, 25]: 10:30 A.M. // [28, 32]: EOD
    truck.loadPackages([6, 25, 28, 32])

    # Extra packages to be loaded (EOD)
    truck.loadPackages([35, 39, 10, 11, 12])


def reloadTruckTwoPackages(truck):
    # TRUCK 2 (EOD)
    truck.loadPackages([17, 21, 22, 23, 24, 26, 27, 33])

    # Correct address unknown until 10:20 A.M. (EOD)
    truck.loadPackages([9])
