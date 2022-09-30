from Node import Node

class SingleLinkedList():
    def __init__(self, value) -> None:
        node = Node(value)
        self.head = node
        self.tail = self.head
        self.length = 1


    def append_item (self, value):
        new_node: Node = Node(value)
        self.tail.next = new_node
        self.tail = new_node
        self.length += 1

        return self

    def prepend_item(self, value):
        new_node: Node = Node(value)
        new_node.next = self.head
        self.head = new_node
        self.length += 1

        return self

    def list_length(self):
        return self.length

    def get_value(self, index):
        if index > self.length - 1:
            raise Exception('Index does not exist')

        node = self.head
        for i in range(index):
            if i == index:
                break
            node = node.next
        
        return node.get_value()

    def insert(self, value, position):
        if position > self.length:
            raise Exception('Index does not exist')
        elif position == 0:
            self.prepend_item(value)
            return self
        elif position == self.length:
            self.append_item(value)
            return self

        new_node = Node(value)
        node = self.head

        for i in range(position+1):
            if i == position:
                new_node.next = node.next
                node.next = new_node
                self.length += 1
                break

            node = node.next

        return self

    def print_list(self):
        node = self.head
        print('-----')
        for i in range(self.length):
            print(f'value: {node.get_value()}')
            node = node.next
    
    def delete(self,index):
        node:Node = self.head
        for i in range(index + 1):
            if i == index:
                node.next = node.next.next
                self.length -= 1
                break
            node = node.next
        return self

    def find(self, value):

        node = self.head
        for _ in range(self.length):
            print(f'node value: {node.get_value()}')
            if value == node.get_value():
                return 'element exist in the list'
            node = node.next

        raise Exception('Element does not exist in the list')

def main():
    new_s_l_l = SingleLinkedList(2)
    new_s_l_l.append_item(3)
    new_s_l_l.prepend_item(1)

    print(f'length: {new_s_l_l.list_length()}')
    # print(f'value index 1: {new_s_l_l.get_value(1)}')
    # print(f'value index 0: {new_s_l_l.get_value(1)}')
    new_s_l_l.print_list()
    new_s_l_l.insert(value=6,position=0)
    # print(f'value index 1: {new_s_l_l.get_value(1)}')
    new_s_l_l.insert(value=63,position=4)
    new_s_l_l.print_list()
    new_s_l_l.delete(1)
    new_s_l_l.print_list()
    print(new_s_l_l.find(63))
    print(new_s_l_l.find(630))

if __name__ == '__main__':
    main()    