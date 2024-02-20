# Class used for storing and manipulating packages in a hash table using chaining
class HashTable:

    # Constructor for hash table with default initial capacity set to 40
    # The default capacity refers to the number of packages to be delivered
    # Each bucket is initially assigned an empty list
    def __init__(self, initialCapacity = 40):
        # Begin initializing hash table with empty bucket list entries
        self.table = []
        for i in range(initialCapacity):
            self.table.append([])

    # This method hashes the item and places it into the appropriate bucket
    # Chaining is used if applicable
    def insert(self, item):
        # The item's bucket is the result of first hashing the data into numerical form
        # and then performing 'the resulting hash' mod table length (in this case 40)
        bucket = hash(item) % len(self.table)

        # The prior resulting bucket is used to pull the bucket list from the table
        # The item is then appended to the bucket's list
        bucketList = self.table[bucket]
        bucketList.append(item)

    # This method searches for the item by hashing the key and searching the returned bucket list
    def search(self, key):
        # The item's bucket is found by hashing the key then performing 'hash mod table length'
        # The bucket list is found by retrieving the list stored in the bucket
        bucket = hash(key) % len(self.table)
        bucketList = self.table[bucket]

        # Search for a matching key in the bucket list
        if key in bucketList:
            # If the key is found, retrieve the item from its found index
            itemIndex = bucketList.index(key)
            return bucketList[itemIndex]
        else:
            # The key was not found
            return None


