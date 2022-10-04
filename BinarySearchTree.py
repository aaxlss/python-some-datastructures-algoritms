from TreeNode import TreeNode

class BinarySearchTree():
    def __init__(self) -> None:
        self.root = None

    def insert(self, value):
        new_node = TreeNode(value)

        if self.root is None:
            self.root = new_node
        else:
            current_node = self.root
            while True:
                if value < current_node.value:
                    if current_node.left == None:
                        current_node.left = new_node
                        return current_node
                    else:
                        current_node = current_node.left
                else:
                    if current_node.right == None:
                        current_node = new_node
                        return current_node
                    else:
                        current_node = current_node.right
        return self



    def lookup(self, value):
        if self.root is None:
            raise Exception('No values in BST')

        current_node = self.root
        while current_node !=  None:
            if current_node.value == value:
                return current_node
            elif value < current_node.value:
                current_node = current_node.left
            else:
                current_node = current_node.right
        return False

    def delete(self, value):
        pass

def main():
    bst = BinarySearchTree()
    print(bst.insert(9))
    print(bst.insert(19))
    print(bst.insert(29))
    print(bst.insert(93))
    print(bst.insert(59))
    print(bst.insert(79))
    print(bst.insert(93))

    print(bst.lookup(10000))
    print(bst.lookup(79))
if __name__ == '__main__':
    main()