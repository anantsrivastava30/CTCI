class Node:

    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_next(self, new_next):
        self.data = new_next


class LinkedList:

    def __init__(self, head=None):
        self.head = head

    def __iter__(self):
        current = self.head
        while current is not None:
            yield current
            current = current.next

    def insert(self, data):
        node = Node(data)
        p = self.head
        if p is None:
            self.head = node
            return
        else:
            while p.next is not None:
                p = p.next
            p.next = node

    def display(self):
        p = self.head
        if p is None:
            print("list is Empty")
            return
        else:
            s = "List:" + " -> ".join([str(node.data) for node in self])
            print(s)


def remove_dup(list):
    p = list.head
    hash = {p.data: True}
    while p.next is not None:
        if p.next.data in hash:
            p.next = p.next.next
        else:
            p = p.next
            hash[p.data] = True


def disp_k(head, k):
    if head is None:
        return 0
    i = disp_k(head.next, k) + 1
    if i <= k:
        print(head.data)
    return i


def list_sum(list1, list2):
    p1 = list1.head
    p2 = list2.head
    if p1 is None or p2 is None:
        print("error")
        return
    carry = 0
    sum = LinkedList()
    while p1 or p2 is not None:
        if p1 and p2 is not None:
            x = (p1.data + p2.data) % 10
            print(x+carry)
            sum.insert(x + carry)
            if p1.data + p2.data > 9:
                carry = 1
            else:
                carry = 0
            p1, p2 = p1.next, p2.next

        if p1 is None and p2 is not None:
            sum.insert(p2.data+carry)
            carry = 0
            p2 = p2.next
        if p2 is None and p1 is not None:
            sum.insert(p1.data+carry)
            carry = 0
            p1 = p1.next
    if carry is 1:
        sum.insert(1)

    sum.display()


def list_sum_recr(l1,l2,sum):
    if not l1.head or not l2.head:
        return 0, 0
    else:
        a, carry = list_sum_recr(l1.head.next, l2.head.next, sum)
        x = l1.head.data + l2.head.data + carry
        if x > 10:
            carry = 1
        else:
            carry = 0
            sum.insert(x % 10)
        return x%10, carry
        



def main():
    l = LinkedList()
    l.insert(1)
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
    """
    remove_dup(l)

    print("______________________________")
    l2 = LinkedList()
    l3 = LinkedList()
    l2.insert(7);l2.insert(1);l2.insert(6)
    l3.insert(5);l3.insert(9);l3.insert(2)
    # print(l2.head.data,l3.head.data)
    list_sum(l2,l3)
    l4 = LinkedList()
    print("______________________________")
    """

if __name__ == "__main__":
    main()





