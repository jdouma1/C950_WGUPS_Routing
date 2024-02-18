class HashTable:
    def __init__(self, initialCapacity = 40):
        self.table = []

        for i in range(initialCapacity):
            self.table.append([])

