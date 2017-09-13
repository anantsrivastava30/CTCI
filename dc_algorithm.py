__author__ = 'Anant'


"""
This class makes the node to a singly lined list
"""


class SinglyLinkedNode(object):

    def __init__(self, item=None, next_link=None):
        super(SinglyLinkedNode, self).__init__()
        self._item = item
        self._next = next_link

    @property
    def item(self):
        return self._item

    @item.setter
    def item(self, item):
        self._item = item

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, next_link):
        self._next = next_link

    def __repr__(self):
        return repr(self.item)

"""
This class makes the Singly Linked list
"""


class SinglyLinkedList(object):

    def __init__(self, head=None):
        super(SinglyLinkedList, self).__init__()
        self.head = head
        self.size = 0

    def __len__(self):
        return self.size

    def __iter__(self):
        current = self.head
        while current is not None:
            yield current
            current = current.next

    def __contains__(self, key):
        for item in self:
            if item.item == key:
                return True
        return False

    def remove(self, key):
        current = self.head
        previous = None
        found = False
        # finds the element: Note that we cannot use __contains__()
        # as we need to use the OBJECT of the key.
        while current is not None and found is False:
                if current.item == key:
                    found = True
                else:
                    previous = current
                    current = current.next
        # remove if is the element is in the middle or last of the list
        if found is True and previous is not None:
            previous.next = current.next
            self.size -= 1
            print("Successfully removed : ", current.item)
        # remove if is the element is in the middle or last of the list
        elif found is True and previous is None:
            self.head = current.next
            self.size -= 1
            print("Successfully removed : ", current.item)
        elif found is False:
            print("Value not found.!")

    # adding to the list
    def prepend(self, item):
        new_node = SinglyLinkedNode(item, self.head)
        self.head = new_node
        self.size += 1

    def __repr__(self):
        s = "List:" + " -> ".join([str(item.item) for item in self])
        return s

"""
This class object is created to enable a key value paired object
 for the dictionary functions in the hash table and the
 binary tree
"""


class KeyValue:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return str(self.key)+" : "+str(self.value)

"""
This class creates the hash table implemented with a linked list
"""


class ChainedHashDict(object):

    def __init__(self, bin_count=10, max_load=0.7, hashfunc=hash):
        super(ChainedHashDict, self).__init__()
        i = 0
        self._bin_count = bin_count
        self._load_factor = max_load
        self.list = []
        while i < self.bin_count:
            self.list.append(SinglyLinkedList())
            i += 1
        self._hashfunc = hashfunc

    @property
    def hashfunc(self):
        return self._hashfunc

    @hashfunc.setter
    def hashfunc(self, hashfunc):
        self._hashfunc = hashfunc

    @property
    def load_factor(self):
        return float(self.__len__())/float(self.bin_count)

    @property
    def bin_count(self):
        return self._bin_count

    @bin_count.setter
    def bin_count(self, bin_count):
        self._bin_count = bin_count

    # It forms a new table and passes it to the existing table
    # it has a hash func to test for terrible hash
    def rebuild(self, bincount, hashfunc=hash):
        new = ChainedHashDict(bincount)
        new.hashfunc = hashfunc
        for i in self.list:
            for item in i:
                if item:
                    new.__setitem__(item.item.key, item.item.value)
                    self.__delitem__(item.item.key)
        return new

    def __getitem__(self, key):
        h = int(self.hashfunc(key)) % self._bin_count
        bucket = self.list[h]
        for kv in bucket:
            if kv.item.key == key:
                return kv.item.value
        return False

    # it sets the item as a linked node so that a linked
    # list can be used
    # it prints a message when load factor is exceeded
    def __setitem__(self, key, value):
        if self.__contains__(key):
            raise Exception("List has the element!")
        h = int(self.hashfunc(key)) % self._bin_count
        self.list[h].prepend(KeyValue(key, value))
        if self.load_factor > self._load_factor:
            print("Load factor exceeded!, proceed with rebuild")

    # deletes the key from the linked list
    def __delitem__(self, key):
        h = int(self.hashfunc(key)) % self._bin_count
        bucket = self.list[h]
        current = bucket.head
        previous = None
        found = False
        while current is not None and found is False:
                if current.item.key == key:
                    found = True
                else:
                    previous = current
                    current = current.next
        if found is True and previous is not None:
            previous.next = current.next
            self.list[h].size -= 1
            return current.item
        elif found is True and previous is None:
            self.list[h].head = current.next
            self.list[h].size -= 1
            return current.item
        elif found is False:
            return "Key not found.!"

    def __contains__(self, key):
        h = int(self.hashfunc(key)) % self._bin_count
        bucket = self.list[h]
        for kv in bucket:
            if kv.item.key == key:
                return True
        return False

    # I have used a counter for counting the elements
    def __len__(self):
        count = 0
        for i in self.list:
            count += i.__len__()
        return count

    def display(self):
        # TODO: Return a string showing the table with multiple lines
        # TODO: I want the string to show which items are in which bins
        print("----------Displaying Chained HashDict------------")
        count = 0
        for i in self.list:
            print("Bin" + "[" + str(count) + "] : " + i.__repr__())
            count += 1

"""
This class creates the hash table implemented through Double Hashing
"""


class OpenAddressHashDict(object):

    # I have used two functions to hash keys 1. hash() 2. id()
    def __init__(self, bin_count=10, max_load=0.7, hashfunc1=hash,
                 hashfunc2=id):
        super(OpenAddressHashDict, self).__init__()
        i = 0
        self._bin_count = bin_count
        self._load_factor = max_load
        self.list = []
        while i < self.bin_count:
            self.list.append([])
            i += 1
        self.hash1 = hashfunc1
        self.hash2 = hashfunc2

    @property
    def load_factor(self):
        return float(self.__len__())/float(self.bin_count)

    @property
    def bin_count(self):
        return self._bin_count

    # This function has a hash parameter in its declaration
    # It forms a new table and passes it to the existing table
    def rebuild(self, bincount, hashfunc1=hash, hashfunc2=id):
        new = OpenAddressHashDict(bincount)
        new.hash1 = hashfunc1
        new.hash2 = hashfunc2
        for i in self.list:
            if i:
                new.__setitem__(i.key, i.value)
                self.__delitem__(i.key)
        return new

    def __getitem__(self, key):
        i = 0
        flag = False
        while flag is False:
            h = (self.hash1(key) + i*self.hash2(key)) % self.bin_count
            if not self.list[h]:
                return "object is absent"
            elif self.list[h].key == key:
                return self.list[h]
            else:
                i += 1

    # Method uses a flag to iterate and find a suitable position in
    # the hash table
    def __setitem__(self, key, value):
        if self.__contains__(key):
            raise Exception("Key Value is already present in the dict")
        i = 0
        flag = False
        while flag is False:
            h = (self.hash1(key) + i*self.hash2(key)) % self.bin_count
            if self.list[h] and self.list[h].key is not None:
                i += 1
            else:
                self.list[h] = KeyValue(key, value)
                flag = True
        if self.load_factor > self._load_factor:
            print("Load factor exceeded!, proceed with rebuild")

    # same functionality as __setitem__() but deletes and sets the
    # value of the deleted key as False enabling deletion in
    # open Addressing
    def __delitem__(self, key):
        i = 0
        flag = False
        while flag is False:
            h = (self.hash1(key) + i*self.hash2(key)) % self.bin_count
            if not self.list[h] or self.list[h] is False:
                return "object is absent"
            elif self.list[h].key == key:
                self.list[h] = KeyValue(None, None)
            else:
                i += 1

    def __contains__(self, key):
        i = 0
        flag = False
        while flag is False:
            h = (self.hash1(key) + i*self.hash2(key)) % self.bin_count
            if not self.list[h]:
                return False
            elif self.list[h].key == key:
                return True
            else:
                i += 1

    def __len__(self):
        count = 0
        for i in self.list:
            if i:
                count += 1
        return count

    def display(self):
        # TODO: Return a string showing the table with multiple lines
        # TODO: I want the string to show which items are in which bins
        count = 0
        for i in self.list:
            print("Bin[", count, "] :", i)
            count += 1

"""
This class object is created to enable a node for a binary
search tree
"""


class BinaryTreeNode(object):
    def __init__(self, data=None, left=None, right=None, parent=None):
        super(BinaryTreeNode, self).__init__()
        self.data = data
        self.left = left
        self.right = right
        self.parent = parent

"""
This class creates a Binary search Tree
"""


def minimum(x):
    while x.left is not None:
        x = x.left
    return x


class BinarySearchTreeDict(object):

    def __init__(self, head=None):
        super(BinarySearchTreeDict, self).__init__()
        self._height = 0
        self.head = head

    # recursively finds the height of the tree
    def height(self, node):
        if node is None:
            return 0
        else:
            return max(self.height(node.left), self.height(node.right)) + 1

    # Recursively returns the key value pairs as object generators in-orderly
    def inorder_keys(self, node):
        if node.left:
            for elem in self.inorder_keys(node.left):
                yield elem
        yield node
        if node.right:
            for elem in self.inorder_keys(node.right):
                yield elem

    # Recursively returns the key value pairs as object generators post-orderly
    def postorder_keys(self, node):
        if node.left:
            for elem in self.postorder_keys(node.left):
                yield elem
        if node.right:
            for elem in self.postorder_keys(node.right):
                yield elem
        yield node

    # Recursively returns the key value pairs as object generators pre-orderly
    def preorder_keys(self, node):
        yield node
        if node.left:
            for elem in self.preorder_keys(node.left):
                yield elem
        if node.right:
            for elem in self.preorder_keys(node.right):
                yield elem

    def items(self):
        lis = self.inorder_keys(self.head)
        print("Key Value Pairs in In-order form :")
        for i in lis:
            print(i.data)

    def __getitem__(self, key):
        if self.head:
            return self.get(self.head, key)
        else:
            return "Tree is Empty!"

    def get(self, node, key):
        value = False
        if key == node.data.key:
            return True
        elif key < node.data.key:
            if node.left is None:
                return False
            else:
                value = self.get(node.left, key)
        elif key > node.data.key:
            if node.right is None:
                return False
            else:
                value = self.get(node.right, key)
        return value

    # relies on a secondary function to recurse
    def __setitem__(self, key, value):
        new_node = BinaryTreeNode(KeyValue(key, value))
        if self.head:
            self.insert(self.head, new_node)
        else:
            self.head = new_node

    def insert(self, node, new_node):
        if new_node.data.key < node.data.key:
            if node.left is None:
                node.left = new_node
                node.left.parent = node
            else:
                self.insert(node.left, new_node)
        elif new_node.data.key > node.data.key:
            if node.right is None:
                node.right = new_node
                node.right.parent = node
            else:
                self.insert(node.right, new_node)

    # Transplants a node u to a node v
    def transplant(self, u, v):
        if u.parent is None:
            self.head = v
        elif u is u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        if v is not None:
            v.parent = u.parent

    # uses transplant to delete a node successfully
    def __delitem__(self, key):
        if self.__contains__(key):
            node = self.__contains__(key)
            if node.left is None:
                self.transplant(node, node.right)
            elif node.right is None:
                self.transplant(node, node.left)
            else:
                y = minimum(node.right)
                if y.parent is not node:
                    self.transplant(y, y.right)
                    y.right = node.right
                    y.right.parent = y
                self.transplant(node, y)
                y.left = node.left
                y.left.parent = y
        else:
            print('tree does not have key')

    def __contains__(self, key):
        if self.head:
            return self.contains(self.head, key)
        else:
            return "Tree is Empty!"

    def contains(self, node, key):
        value = False
        if key == node.data.key:
            return node
        elif key < node.data.key:
            if node.left is None:
                return False
            else:
                value = self.contains(node.left, key)
        elif key > node.data.key:
            if node.right is None:
                return False
            else:
                value = self.contains(node.right, key)
        return value

    def __len__(self):
        node = self.head
        return self.height(node)

    def display(self):
        # TODO: Print the keys using INORDER on one
        # line and PREORDER on the next
        print("Inorder representation of keys : ",
            [i.data.key for i in self.inorder_keys(self.head)])
        print("Pre-order representation of keys : ",
            [i.data.key for i in self.preorder_keys(self.head)])

"""
This method creates a terrible hash function which returns a given value
irrespective of the value passed
"""


def terrible_hash(bin):
    """A terrible hash function that can be used for testing.

    A hash function should produce unpredictable results,
    but it is useful to see what happens to a hash table when
    you use the worst-possible hash function.  The function
    returned from this factory function will always return
    the same number, regardless of the key.

    :param bin:
        The result of the hash function, regardless of which
        item is used.

    :return:
        A python function that can be passes into the constructor
        of a hash table to use for hashing objects.
    """
    def hashfunc(item):
        return bin
    return hashfunc


def main():
    c = SinglyLinkedList()
    print("--------------New Linked List---------------------")
    print(c.__repr__())
    c.prepend(2)
    c.prepend(3)
    c.prepend(4)
    c.prepend(5)
    c.prepend(6)
    c.prepend(7)
    c.prepend(8)
    print(c.__repr__())
    print("List contains the element: 4: ", c.__contains__(4))
    print(c.__len__())
    c.remove(4)
    print(c.__len__())
    print(c.__repr__())
    print("List contains the element: 4: ", c.__contains__(4))
    binary_count = 10
    e = ChainedHashDict()
    print("--------------New Chained Dictionary---------------")
    e.__setitem__("wolber", "359-4787")
    e.__setitem__("reblow", "akfj-askf")
    e.__setitem__("ravage", "539-9692")
    e.__setitem__("qeblow", "khjg-kjbk")
    e.__setitem__("alpha", "123-856")
    e.__setitem__("fiat", "quan-tash")
    e.__setitem__("mist", "mag-mist")
    e.__setitem__("dodo", "456-7963")
    e.display()
    print("Load factor before the rebuild :", e.load_factor)
    print("New table with binary count increased :")
    e = e.rebuild(binary_count*2)
    e.display()
    print("Load factor after the rebuild :", e.load_factor)
    print("Number of values stored in the Dict : ", e.__len__())
    print("Deleted Key : Value  pair is ", e.__delitem__("dodo"))
    e.display()
    print("Number of values stored in the Dict after the delete :"
          " ", e.__len__())
    e.__setitem__("dodo", "456-7963")
    print("--------------New Open Addressing Dictionary---------------")
    # f = OpenAddressHashDict()
    # f.__setitem__("wolber", "359-4787")
    # f.__setitem__("reblow", "akfj-askf")
    # f.__setitem__("qeblow", "khjg-kjbk")
    # f.__setitem__("alpha", "123-856")
    # f.__setitem__("fiat", "quan-tash")
    # f.__setitem__("mist", "mag-mist")
    # f.__setitem__("dodo", "456-7963")
    # f.__setitem__("ravage", "539-9692")
    # print(f.__getitem__("reblow"))
    # f.__delitem__("reblow")
    # print(f.__getitem__("reblow"))
    # f.display()
    # f.__setitem__("reblow", "akfj-askf")
    # print("Load factor before the rebuild :", f.load_factor)
    # f = f.rebuild(20)
    # f.display()
    # print("Load factor after the rebuild :", f.load_factor)

    print("--------------New Binary Search Tree---------------------")
    a = BinarySearchTreeDict()
    print("Checking if the new created is empty : ", a.__getitem__(3))
    a.__setitem__(500, "234")
    a.__setitem__(250, "234sf")
    a.__setitem__(489, "234sfd")
    a.__setitem__(600, "234")
    a.__setitem__(650, "234sf")
    a.__setitem__(800, "234sfd")
    a.__setitem__(129, "234sfd")
    a.__setitem__(499, "234sf")
    a.__setitem__(312, "234sfd")
    a.__setitem__(1001, "234sfd")
    # checking if tree can delete key!
    a.__delitem__(200)
    # actually deleting value
    a.display()
    print("after Deleting the Tre looks like! :")
    a.__delitem__(250)
    a.display()
    a.items()
    print("the length of the Tree :", a.__len__())
    print("------------------Testing Terrible Hash-----------------------")
    e = e.rebuild(binary_count, terrible_hash(9))
    e.display()
    # f = f.rebuild(binary_count, terrible_hash(10), terrible_hash(10))
    # this fucntion maps all the keys to a single node and thus causes
    # a infinite loop so I have Commented this


if __name__ == '__main__':
    main()
