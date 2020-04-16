class Node:
    def __init__(self, data=None):
        self.prev = None
        self.data = data
        self.next = None


class DoublyLinkedList:
    def __init__(self):
        self.tail = None
        self.head = None

    def insert(self, x):
        NewNode = Node(x)
        NewNode.next = self.head
        if self.head is not None:
            self.head.prev = NewNode
        self.head = NewNode
        NewNode.prev = None

    def delete(self, x):
        DelNode = self.search(x)
        if DelNode.prev is not None:
            DelNode.prev.next = DelNode.next
        else:
            self.head = x.next
        if DelNode.next is not None:
            DelNode.next.prev = DelNode.prev

    def search(self, k):
        x = self.head
        while x is not None and x.data != k:
            x = x.next
        return x

    def list_print(self):
        print_val = self.head
        while print_val:
            print(print_val.data)
            print_val = print_val.next
