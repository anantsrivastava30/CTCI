import collections
from bitarray import bitarray

# CTCI problems

def check_duplicate():
    f = open("duplicate string.txt", 'r')
    text = f.read()
    text = set(text)
    checker = 0
    a = bitarray(127)
    print(a.length())
    for word in text:
        var = ord(word) - ord(' ')
        if checker & (1 << var) > 0:
            return False
        else:
            checker |= (1 << var)
    return True


def permute(str1, str2):
    c = collections.Counter(str1)
    d = collections.Counter(str1)
    print(c == d)
    print(sum(c.values()))
    print(16 & 15)


def main():
    print(check_duplicate())
    permute("hello","loleh")


if __name__ == "__main__":
    main()
