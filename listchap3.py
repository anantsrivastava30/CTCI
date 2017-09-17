import math

from numba.tests.test_exceptions import MyError
from numpy import empty


# stack using static array
class Stack:
    def __init__(self):
        self.__items = empty(10, dtype=object)
        self.__top = -1

    def __repr__(self):
        return str(self.__items)

    def isEmpty(self):
        return self.__top == -1

    def push(self, data):
        try:
            if data < self.min():
                self.__top += 1
                self.__items[self.__top] = (NodeMin(data, data))
            else:
                val = self.min()
                self.__top += 1
                self.__items[self.__top] = (NodeMin(data, val))
        except IndexError:
            print("stack full")

        def pop(self):
            try:
                val = self.__items[self.__top]
                self.__top -= 1
                return val
            except IndexError:
                print("stack empty")

        def peek(self):
            if self.__top != -1:
                return self.__items[self.__top]
            else:
                print("stack empty")

        def size(self):
            return self.__top

    def min(self):
        try:
            if self.isEmpty():
                # print(math.inf)
                return math.inf
            else:
                # print(self.peek(), self.top)
                return self.peek().min
        except IndexError:
            print("stack full")


class Stack2:
    def __init__(self):
        self.items = []
        self.stackWithMin = []

    def isEmpty(self):
        return not self.items

    def __repr__(self):
        return str(self.items)

    def push(self, data):
        if data <= self.min():
            self.stackWithMin.append(data)
        self.items.append(data)

    def pop(self):
        try:
            if self.peek() is self.min():
                self.stackWithMin.pop()
            return self.items.pop()
        except IndexError:
            print("List is Empty!!")

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

    def min(self):
        if self.isEmpty():
            return math.inf
        else:
            return self.stackWithMin[len(self.stackWithMin) - 1]


class NodeMin:
    def __init__(self, data=0, min=math.inf):
        self.data = data
        self.min = min


def func1():
    raise MyError('This is an error')


def main():
    a = Stack()
    a.push(3)
    a.push(1)
    a.push(0)
    a.push(6)
    a.push(-2)
    a.push(3)
    a.push(1)
    a.push(0)
    a.push(6)


if __name__ == "__main__":
    main()

