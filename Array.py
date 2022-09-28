from array import array


class Array:
    
    def __init__(self) -> None:
        self.length = 0
        self.data = {}

    def get(self, index):
        return self.data[index]

    def push(self,item):
        self.data[self.length] = item
        self.length += 1

        return self.length

    def pop(self):
        last_item = self.data[self.length - 1]
        del self.data[self.length - 1]
        self.length -= 1
        return last_item

    def delete(self, index):
        item = self.data[index]
        self.shiftItem(index)
        return item

    def shiftItem(self, index):
        for i in range(index, self.length - 1):
            self.data[i]  = self.data[ i + 1]

        del self.data[self.length - 1]
        self.length -= 1

def main():
    array_obj = Array()
    array_obj.push('a')
    array_obj.push('hello')
    array_obj.push('b')
    array_obj.push('c')
    array_obj.push('d')
    # print(array_obj.length)
    print(array_obj.data)
    # print(array_obj.get(0))
    array_obj.delete(3)
    print(array_obj.data)
    pass
if __name__ == '__main__':
    main()