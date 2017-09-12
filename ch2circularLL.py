import os
import sys
from chapter2 import LinkedList


class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class CircularLinkedList:
    def __init__(self, head=None):
        self.head = head

    def __iter__(self):
        current = self.head
        while current.next is not self.head:
            yield current
            current = current.next
        yield current

    def insert(self, data):
        node = Node(data)
        current = self.head
        if current is None:
            self.head = node
            node.next = node
            return
        else:
            first = current
            while current.next is not first:
                current = current.next
            current.next = node
            node.next = first

    def display(self):
        if self.head is None:
            print("list is empty")
            return
        else:
            print("List:" + "->".join([str(node.data) for node in self]))


def corrupt(list):
    slow = list.head
    fast = list.head
    if list.head is None:
        print("Lost is empty")
        return
    while fast is not None and slow is not None:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break
    slow = list.head
    while slow is not fast:
        slow = slow.next
        fast = fast.next

    return slow.data


def palindrome(list):
    slow = list.head
    fast = slow
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

    current = list.head

    stack = []
    while current is not slow:
        stack.append(current.data)
        current = current.next

    while slow is not None:
        if slow.data != stack.pop():
            return False
        slow = slow.next

    return True



def main():
    l = CircularLinkedList()
    l.insert(6)
    l.insert(2)
    l.insert(3)
    l.insert(4)
    l.insert(5)
    l.insert(6)
    l.insert(1)
    l.insert(2)
    l.insert(3)
    l.insert(4)
    l.insert(5)
    l.insert(6)
    l.display()
    print(corrupt(l))
    # print(os.path.dirname(os.path.realpath(__file__)))
    # print(sys.version)
    l = LinkedList()
    l.insert(1)
    l.insert(2)
    l.insert(3)
    l.insert(3)
    l.insert(2)
    l.insert(8)
    print(palindrome(l))


if __name__ == "__main__":
    main()
