import time
import math
"""
INPUT:
3
1 1 2
1
1 4 5
3
2 3 9
6 2

OUTPUT:
[1, 8, 6]
"""

def cake():
    # number of test cases
    t = int(input())
    if t < 1 or t > 100:
                return "Invalid Testcase"
    out = []
    for i in range(t):
        var = input()
        data = list(map(int, var.split()))
        # number of friends
        f = data[0]
        if f < 1 or f > 500:
                return "Invalid Friends"
        # Height of the cake
        h = data[1]
        if h < 1 or h > 1000:
                return "Invalid height"
        # Width of the cake
        w = data[2]
        if w < 1 or w > 1000:
                return "Invalid Weight"

        # partitions of cake according to friends
        var1 = input()
        y = list(map(int, var1.split()))
        y.sort()
        l = 0
        min = math.inf
        for i in y:
            l = h * i - l
            if l < min:
                min = l

        l = (w - y[len(y)-1]) * h
        if l < min:
            min = l
        out.append(min)
    return out


start_time = time.time()


def main():
    print (cake())

if __name__ == "__main__":
    main()


print("--- %s seconds ---" % (time.time() - start_time))
