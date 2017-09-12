import networkx as nx
import hashlib
from collections import deque
import matplotlib.pyplot as plt
from numba.tests.test_exceptions import MyError
from sympy import floor


def height(root):
    if not root:
        return 0
    leftheight = height(root.left)
    if leftheight == -1:
        return -1

    rightheight = height(root.right)
    if rightheight == -1:
        return -1

    diff = rightheight - leftheight
    if abs(diff) > 1:
        return -1
    else:
        return max(leftheight, rightheight) + 1


def route(graph, start, end):
    dict = {i: "Unvisited" for i in graph.nodes()}
    queue = deque([])
    dict[start] = "Visiting"
    queue.append(start)
    while queue:
        u = queue.popleft()
        if u is not None:
            for v in graph.neighbors(u):
                if dict[v] is "Unvisited":
                    if v == end:
                        return True
                    else:
                        dict[v] = "Visiting"
                        queue.append(v)
            dict[u] = "Visited"

    return False


class Node(object):
    def __init__(self, data):
        self.__data = data
        self.__left = None
        self.__right = None

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data

    @property
    def left(self):
        return self.__left

    @left.setter
    def left(self, left):
        self.__left = left

    @property
    def right(self):
        return self.__right

    @right.setter
    def right(self, right):
        self.__right = right


def BST(arr, low, high):
    if high < low:
        return None
    mid = int((low + high)/2)
    n = Node(arr[mid])
    n.left = BST(arr, low, mid-1)
    n.right = BST(arr, mid+1, high)
    return n


def minimalBST(arr):
    return BST(arr, 0, len(arr)-1)


def inorder(node):
    yield node
    if node.left:
        for elem in inorder(node.left):
            yield elem

    if node.right:
        for elem in inorder(node.right):
            yield elem


def levellinkedlist(root, lists, level):
    if root is None:
        return
    list = []
    if len(lists) == level:
        lists.append(list)
    else:
        list = lists[level]
    list.append(root)
    levellinkedlist(root.left, lists, level + 1)
    levellinkedlist(root.right, lists, level + 1)


def isbst(root, min, max):
    if root is None:
        return True

    if root.data <= min or root.data > max:
        return False

    if not isbst(root.left, min, root.data) or not isbst(root.right, root.data, max):
        return False

    return True


def hastree(tree1, tree2):
    if tree2 is None:
        return True
    return subtree(tree1, tree2)


def subtree(tree1, tree2):
    if tree1 is None:
        return False
    if tree1.data == tree2.data:
        if comparetrees(tree1, tree2):
            return True
    return subtree(tree1.left, tree2) or subtree(tree1.right, tree2)


def comparetrees(tree1, tree2):
    if not tree1 and not tree2:
        return True
    elif not tree1 or not tree2:
        return False
    if tree1.data != tree2.data:
        return False
    return comparetrees(tree1.left, tree2.left) and comparetrees(tree1.right, tree2.right)



def main():
    f = open("text.txt", encoding='utf-8')
    list = []
    text = f.read()
    fulltext = text.split("\n")
    for line in fulltext:
        h = hashlib.sha1(line.encode())
        list.append(h.hexdigest())
    print(list)
    g = nx.DiGraph()
    g.add_edge(1, 2, weight=2)
    g.add_edge(1, 3, weight=5)
    g.add_edge(2, 4, weight=34)
    g.add_edge(3, 5, weight=65)
    g.add_node(7)
    print(i.get_edge_data() for i in g.neighbors(4))
    print(route(g,1,5))
    list = [0,1,2,3,4,5,6]
    root = minimalBST(list)
    l = []*height(root)
    levellinkedlist(root, l, 0)
    print(root.data, root.left.data, root.right.data)
    print(isbst(root, -1, 10))
    print(hastree(root, root.left))


    """
    nx.draw(g)
    nx.draw_networkx_labels(g, pos=nx.spring_layout(g))
    plt.show()
    """
if __name__ == '__main__':
    main()