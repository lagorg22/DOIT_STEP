# დაწერეთ value გადაწოდების შედეგად ამოშლის ლოგიკა დაკავშირებულ სიებში და ინდექსით ჩამატების ლოგიკა

class ListNode:
    def __init__(self, val=None):
        self.val = val
        self.next: ListNode = None

class LinkedList:
    def __init__(self):
        self.__head: ListNode = None
        self.__size: int = 0

    def size(self) -> int:
        return self.__size

    def append(self, val):
        node = ListNode(val)
        if not self.__head:
            self.__head = node
        else:
            tmp_node: ListNode = self.__head
            while tmp_node.next:
                tmp_node = tmp_node.next
            tmp_node.next = node
        self.__size += 1

    def insert(self, val, idx: int):
        if idx < 0 or idx > self.__size:
            raise IndexError("Index out of range")

        node = ListNode(val)
        if idx == 0:
            node.next = self.__head
            self.__head = node
        else:
            tmp_node: ListNode = self.__head
            idx -= 1
            while idx:
                tmp_node = tmp_node.next
                idx -= 1

            node.next = tmp_node.next
            tmp_node.next = node

        self.__size += 1

    def remove_at(self, idx):
        if idx < 0 or idx >= self.__size:
            raise IndexError("Index out of range")


        if idx == 0:
            self.__head = self.__head.next
        else:
            node: ListNode = self.__head
            idx -= 1
            while idx:
                node = node.next

            if node.next.next:
                node.next = node.next.next
            else:
                node.next = None
        self.__size -= 1

    def contains(self, val) -> bool:
        node: ListNode = self.__head
        while node:
            if node.val == val:
                return True
            node = node.next

        return False

    def remove(self, val):
        if not self.contains(val):
            raise ValueError('This element is not present in the list.')

        node: ListNode = self.__head
        if node.val == val:
            self.__head = self.__head.next
        else:
            while node.next:
                if node.next.val == val:
                    break
                node = node.next

            node.next = node.next.next

        self.__size -= 1

    def display(self):
        lst = []
        node: ListNode = self.__head
        while node:
            lst.append(str(node.val))
            node = node.next

        print('->'.join(lst))


node = LinkedList()

for i in range(20):
    node.append(i)

node.display()
print(node.size())

node.insert(55, 0)
node.insert(32, 21)

node.display()
print(node.size())

# node.insert(32, 55) #Error code

node.remove(3)
node.remove(2)
node.remove(55)

node.display()
print(node.size())

print(node.contains(6))
print(node.contains(432432))

node.remove_at(1)
node.remove_at(0)
print(node.size())

# node.remove_at(50) #error code

node.display()

# node.remove(777) #error code






