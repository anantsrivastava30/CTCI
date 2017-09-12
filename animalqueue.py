from collections import deque
from itertools import permutations


class Animal(object):
    def __init__(self, n):
        self.name = n
        self.order = 0

    def setorder(self, ord):
        self.order = ord

    def getorder(self):
        return self.order

    def isolder(self, a):
        return self.order < a.getorder()


class Dog(Animal):
    def __init__(self, n):
        assert isinstance(self, Animal)
        super().__init__(n)


class Cat(Animal):
    def __init__(self, n):
        assert isinstance(self, Animal)
        super().__init__(n)


class AnimalQueue(object):
    def __init__(self):
        self.dogs = deque([])
        self.cats = deque([])
        self.order = 0

    def enque(self, a):
        a.setorder(self.order)
        self.order += 1
        if isinstance(a, Dog): self.dogs.append(a)
        elif isinstance(a, Cat): self.cats.append(a)

    def dequeany(self):
        if not self.dogs:
            return self.dequecats()
        elif not self.cats:
            return self.dequedogs()

        dog = self.dogs[0]
        cat = self.cats[0]
        if dog.isolder(cat):
            return self.dequedogs()
        else:
            return self.dequecats()

    def dequedogs(self):
        return self.dogs.popleft()

    def dequecats(self):
        return self.cats.popleft()


def main():
    dog1 = Dog("Bella")
    dog2 = Dog("stella")
    dog3 = Dog("queella")
    cat1 = Cat("meeo")
    cat2 = Cat("meeowwww")
    queue = AnimalQueue()
    queue.enque(dog1);queue.enque(dog2)
    queue.enque(cat1);queue.enque(cat2)
    print(queue.dequeany().name)
    print(list(permutations([1,2,3],4)))

if __name__ == '__main__':
    main()