from listchap3 import Stack,Stack2


class Tower(object):

    def __init__(self, index):
        self.__disks = Stack()
        self.__index = index

    def index(self):
        return self.__index

    def add(self, data):
        if not self.__disks.isEmpty() and self.__disks.peek().data <= data:
            return "error placing disks"
        else:
            self.__disks.push(data)

    def moveTopTo(self, t):
        top = self.__disks.pop().data
        t.add(top)
        print("Move disk " + str(top) + " from " + str(self.index()) + " to " + str(t.index()))

    def moveDisks(self, n, destination, buffer):
        if n > 0:
            self.moveDisks(n - 1, buffer, destination)
            self.moveTopTo(destination)
            print(x.data for x in destination.__disks)
            buffer.moveDisks(n-1, destination, self)


# sort a stack using 2 stacks 
def sort(s):
    r = Stack2()
    while not s.isEmpty():
        temp = s.pop()
        while not r.isEmpty() and r.peek() > temp:
            s.push(r.pop())
        r.push(temp)
    return r


def main():
    n = 3
    towers = [Tower(i) for i in range(3)]

    for i in range(n-1, -1, -1):
        towers[0].add(i)

    towers[0].moveDisks(n, towers[2], towers[1])

    stack = Stack2()
    stack.push(2)
    stack.push(4)
    stack.push(3)
    stack.push(1)
    print(sort(stack))


if __name__=="__main__":
    main()