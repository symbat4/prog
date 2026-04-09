class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.root = None

    #1 task: to add a data to the beninging of a list
    def add_front(self, data):
        new_node = Node(data)
        new_node.next = self.root
        self.root = new_node

    #2 task: to add a data to the end of a list
    def add_back(self, data):
        new_node = Node(data)
        current = self.root
        while current.next is not None:
            current = current.next
        current.next = new_node

    #3 task: to remove the last data
    def remove_end(self):
        current =self.root
        while current.next.next is not None:
            current = current.next
        current.next = None

    #4 task: to print all nodes
    def print_all(self):
        current = self.root
        while current is not None:
            print(current.data)
            current = current.next

    #5 task: to search a data
    def search(self, data):
        current = self.root
        while current is not None:
            if current.data == data:
                return True
            current = current.next
        return False
    
    #6 task: to insert a data at a given position
    def insert_in_pos(self, data, position):
        new_node = Node(data)
        if position == 0:
            new_node.next = self.root
            self.root = new_node
            return
        
        current = self.root
        for i in range(position - 1):
            if current is None:
                print('Position out of range')
                return
            current = current.next
        new_node.next = current.next
        current.next = new_node

    #7 task: to remove data by its value
    def remove_val(self, data):
        current = self.root
        prev = None
        while current is not None:
            if current.data == data:
                if prev is None:
                    self.root = current.next
                else:
                    prev.next = current.next
                return
            prev = current
            current = current.next
        print('Element is non existent in the lists')

    #8 task: combine two linked lists into one
    def combine(self, other):
        if self.root is None:
            self.root = other.root
            return
        current = self.root
        while current.next is not None:
            current = current.next
        current.next = other.root

    #9 task: reverse a linked list
    def reverse(self):
        prev = None
        current = self.root
        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.root = prev

    #10 task: insertion sort
    def insertion_sort(self):
        sorted_root = None
        current = self.root

        while current is not None:
            next_node = current.next
            sorted_root = self.sorted_insert(sorted_root, current)
            current = next_node

        self.root = sorted_root
    def sorted_insert(self, sorted_root, new_node):
        new_node.next = None

        if sorted_root is None or new_node.data <= sorted_root.data:
            new_node.next = sorted_root
            return new_node
        
        current = sorted_root
        while current.next is not None and current.next.data < new_node.data:
            current = current.next
        
        new_node.next = current.next
        current.next = new_node
        return sorted_root

list1 = LinkedList()
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
list1.root = n1
n1.next = n2
n2.next = n3

list2 = LinkedList()
m1 = Node(1)
m2 = Node(2)
m3 = Node(3)
list2.root = m1
m1.next = m2
m2.next = m3

list1.add_front(0)
list1.add_back(4)
#list1.remove_end()
print(list1.search(5))
#list1.insert_in_pos(1.5, 2)
#list1.remove_val(1)
#list1.combine(list2)
#list1.reverse()
list1.insertion_sort()
list1.print_all()