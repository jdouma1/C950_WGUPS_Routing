import csv
from HashTable import HashTable
from Package import Package


def loadPackageData(fileName):
    with open(fileName) as packages:
        packageData = csv.reader(packages, delimiter=',')
        next(packageData)
        for package in packageData:
            packageId = int(package[0])
            address = package[1]
            city = package[2]
            state = package[3]
            zipCode = int(package[4])
            deliveryDeadline = package[5]
            weight = int(package[6])

            newPackage = Package(packageId, address, city, state, zipCode, deliveryDeadline, weight)
            packageHashTable.insert(packageId, newPackage)


'''packages = [
    [1, 'Avengers: Infinity War'],
    [2, 'Revenge of the Sith'],
    [3, 'A New Hope']
]'''

packageHashTable = HashTable()
if __name__ == '__main__':
    '''
    myHash = HashTable()
    myHash.insert(bestMovies[0][0], bestMovies[0][1])
    print(myHash.table)

    myHash.insert(bestMovies[1][0], bestMovies[1][1])
    print(myHash.table)

    myHash.insert(bestMovies[2][0], bestMovies[2][1])
    print(myHash.table)
    '''
    loadPackageData("Packages.csv")

    for i in range(len(packageHashTable.table) + 1):
        print("Key: {} and Package: {}".format(i+1, packageHashTable.search(i+1)))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
