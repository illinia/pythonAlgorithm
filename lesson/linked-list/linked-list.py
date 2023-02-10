class Node:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


first = Node(1)
second = Node(2)
third = Node(3)
first.next = second
second.next = third
first.value = 6


class LinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            # current = self.head
            # while current.next:
            #     current = current.next
            # current.next = new_node
            self.tail.next = new_node
            self.tail = self.tail.next

    def get(self, idx):
        current = self.head
        for _ in range(idx):
            current = current.next
        return current.value

    def insert(self, idx, value):
        new_node = Node(value)

        if idx == 0:
            new_node.next = self.head
            self.head = new_node
        elif idx < 0:
            print('idx is minus value')

        else:
            current = self.head
            for i in range(idx - 1):
                current = current.next

            new_node.next = current.next
            current.next = new_node

    def remove(self, idx):
        if idx == 0:
            self.head = self.head.next
        elif idx < 0:
            print('idx is minus value')

        else:
            current = self.head
            for i in range(idx - 1):
                print(i)
                current = current.next

            removing_node = current.next

            current.next = removing_node.next

    def insert_back(self, value):
        new_node = Node(value)

        if self.tail is None and self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node


ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.insert(1, 9)
print('end')

ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.append(5)
ll.remove(3)
print('end')
