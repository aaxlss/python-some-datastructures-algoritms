class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None

    def get_value(self):
        return self.value