class HashTable:

    def __init__(self, size) -> None:
        self.data = [None] * size

    def __hash__(self, key) -> int:
        hash = 0
        
        for i in range(len(key)):
            hash = (hash + ord(key[i]) * i) % len(self.data)
        
        return hash

    def set(self, key, value):
        hash = self.__hash__(key=key)
        if hash not in self.data:
            self.data[hash] = []
        self.data[hash] += [key,value]

    def get(self, key):
        hash = self.__hash__(key)
        if key in self.data[hash]:
            return self.data[hash]
        return 'key does not exist'

    def keys(self):
        keys = [self.data[item][0] for item in range(len(self.data)) if self.data[item] is not None]
        return keys

def main():
    myHashTable = HashTable(5)
    myHashTable.set('apples', 100)
    myHashTable.set('oranges', 10)
    print(myHashTable.keys())
    # print(myHashTable.get('apples'))
    # print(myHashTable.get('oranges'))

if __name__ == '__main__':
    main()