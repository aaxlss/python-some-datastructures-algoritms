
from Node import Node


class Queue():
    def __init__(self) -> None:
        self.first = None
        self.last = None
        self.length = 0

    def peek(self):
        return self.first

    def enqueue(self, value):
        
        new_node = Node(value)

        if self.length == 0:
            self.first = new_node
            self.last = new_node
        else:
            new_node.next = self.first
            self.first = new_node
        
        self.length += 1

        return self

    def dequeue(self):
        
        if self.length == 1:
            self.first = None
            self.last = None
        else:
            old_now = self.first
            self.first = old_now.next

        self.length -= 1

        return self


def main():
    pass

if __name__ == '__main__':
    main()