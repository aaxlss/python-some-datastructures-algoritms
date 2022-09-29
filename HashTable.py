from operator import le


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
    # myHashTable = HashTable(5)
    # myHashTable.set('apples', 100)
    # myHashTable.set('oranges', 10)
    # print(myHashTable.keys())
    # print(myHashTable.get('apples'))
    # print(myHashTable.get('oranges'))
    # array = [2,5,1,2,3,5,1,2,4]
    # array = [2,1,1,2,3,5,1,2,4]
    array = [2,3,4,5]

    print(gettingMostRepeatedNumber(array=array))


def gettingMostRepeatedNumber(array):
    
    most_repeated_number = None
    value_most_repeated_number = 1
    # for i in range(len(array)):
    #     if array[i] in dict:
    #         dict[array[i]] += 1
    #     else:
    #         dict[array[i]] = 1
    dict = {array[i]: dict[array[i]] + 1 if array[i] in dict else 1 for i in range(len(array))}
    for key,value in dict.items():
        print(f'key: {key}, value:{value}')
        if value > 1:
            if most_repeated_number is None:
                most_repeated_number = key
                value_most_repeated_number = value
            else:
                if value_most_repeated_number < value:
                    most_repeated_number = key
                    value_most_repeated_number = value

    return most_repeated_number


if __name__ == '__main__':
    main()