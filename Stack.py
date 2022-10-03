from Node import Node

class Stack():
    def __init__(self) -> None:
        self.top = None
        self.bottom = None
        self.length = 0

def peek(self):
    return self.top

def push(self,value):
    new_node = Node(value)
    
    if self.length == 1:
        self.bottom = self.top
    
    now_node = self.top.next
    self.top = new_node
    if self.length == 0:
        self.bottom = new_node

    self.length += 1

    return self

def pop(self):
    
    old_node = self.top

    if self.length == 0:
        raise Exception('No values in the stack')
        
    if self.length == 1:
        self.top = None
        self.bottom = None
    else:
        self.top = old_node.next



    self.length -= 1
    return self


def main():
    pass

if __name__ == '__main__':
    main()