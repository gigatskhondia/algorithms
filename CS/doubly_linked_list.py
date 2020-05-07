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
        new_node = Node(x)
        new_node.next = self.head
        if self.head is not None:
            self.head.prev = new_node
        self.head = new_node
        new_node.prev = None

    def delete(self, x):
        del_node = self.search(x)
        if del_node.prev is not None:
            del_node.prev.next = del_node.next
        else:
            self.head = x.next
        if del_node.next is not None:
            del_node.next.prev = del_node.prev

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
