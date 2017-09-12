import sys
from pylab import *

INFINITY = sys.maxint


def print_neatly(words, M):
    """ Print text neatly.
Parameters
----------
words: list of str
Each string in the list is a word from the file.
M: int
The max number of characters per line including spaces
Returns
-------
cost: number
The optimal value as described in the textbook.
text: str
The entire text as one string with newline characters.
It should not end with a blank line.
Details
-------
Look at print_neatly_test for some code to test the solution.
"""
    # TODO: Solve the problem
    n = words.__len__()
    extra = np.zeros((n, n))
    # compute extra[i, j] for 1<i<j<n.

    for i in range(n):
        extra[i, i] = M - len(words[i])
        for j in range(i + 1, n):
            extra[i, j] = extra[i, j - 1] - len(words[j]) - 1

    lc = np.zeros((n, n))
    # compute lc[i, j] for 1<i<j<n.
    for i in range(n):
        for j in range(n):
            if extra[i, j] < 0:
                lc[i, j] = INFINITY
            elif j == n - 1 and extra[i, j] >= 0:
                lc[i, j] = 0
            else:
                lc[i, j] = extra[i, j] ** 3
    c = np.zeros(n + 1)
    p = np.zeros(n)
    # compute c]j] and p[j] for 1<j<n
    c[-1] = 0
    for j in range(0, n):
        c[j] = INFINITY
        for i in range(0, j):
            if c[i - 1] + lc[i, j] < c[j]:
                c[j] = c[i - 1] + lc[i, j]
                p[j] = i

    text = ''
    # give_line(p, n - 1)
    i = n - 1
    m = [n]

    while p[i] != 0:
        m.append(int(p[i]))
        i = p[i] - 1
    m.append(0)
    print m

    i = len(m) - 1
    while m[i] != n:
        # print x, m[i], m[i-1] - 1
        for q in words[m[i]: m[i - 1]]:
            if q is words[m[i - 1] - 1]:
                text += q
            else:
                text += q + ' '
        if i != 1:
            text += '\n'
        i -= 1
    cost = c[n - 1]
    return cost, text


def give_line(p, j):
    i = p[j]
    if i == 1:
        k = 1
    else:
        k = give_line(p, i - 1) + 1
    print k, i, j
    return k


def main():
    f = open("kubla_kahn.txt")
    maxline = 80
    text = f.read()
    words = text.split()
    f.close()

    (cost, text) = print_neatly(words, maxline)
    fw = open("format.txt", 'w')
    print >> fw, '----------------------'
    print >> fw, 'Print neatly, file name:kubla_kahn.txt'
    print >> fw, '----------------------'
    print >> fw, text
    print >> fw, '----------------------'
    print >> fw, 'cost = ', cost
    print >> fw, '----------------------'
    fw.close()


if __name__ == "__main__":
    main()
