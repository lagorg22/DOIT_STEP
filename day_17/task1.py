#-------------------------------LL-------------------------

class Node:
    #constructor of a node
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    #constructor of LL
    def __init__(self):
        self.head = None

    #method for adding elems to the LL
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        last_node = self.head
        #getting to the tail
        while last_node.next:
            last_node = last_node.next

        last_node.next = new_node

    def remove_at(self, index):
        #bound check
        if index < 0 or self.head is None:
            return

        #case when head needs to be changed
        if index == 0:
            self.head = self.head.next
            return

        current_node = self.head
        current_position = 0

        #getting to the desired node
        while current_node.next and current_position < index - 1:
            current_node = current_node.next
            current_position += 1

        if current_node.next:
            current_node.next = current_node.next.next

    #printing the LL
    def display(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=' -> ')
            current_node = current_node.next

        print()

#------------------------STACK----------------------
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class Stack:
    #constructor
    def __init__(self):
        self.top_node = None
        self.length = 0

    def empty(self):
        return self.length == 0

    def size(self):
        return self.length

    #pushing new node on top of the stack and putting value in it
    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top_node
        self.top_node = new_node
        self.length += 1

    #returning the top node's val and removing it from the stack
    def pop(self):
        if not self.empty():
            popped_item = self.top_node.data
            self.top_node = self.top_node.next
            self.length -= 1
            return popped_item
        else:
            raise IndexError("Stack is empty")
