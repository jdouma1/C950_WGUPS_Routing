from HashTable import HashTable

bestMovies = [
    [1, 'Avengers: Infinity War'],
    [2, 'Revenge of the Sith'],
    [3, 'A New Hope']
]

if __name__ == '__main__':
    myHash = HashTable()
    myHash.insert(bestMovies[0][0], bestMovies[0][1])
    print(myHash.table)

    myHash.insert(bestMovies[1][0], bestMovies[1][1])
    print(myHash.table)

    myHash.insert(bestMovies[2][0], bestMovies[2][1])
    print(myHash.table)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
