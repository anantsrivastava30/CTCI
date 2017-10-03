import sys


class QueenAttack:
    def __init__(self, n, k, rQueen, cQueen, obs):
        self.n = n
        self.k = k
        self.rQueen = rQueen
        self.cQueen = cQueen
        self.obstacle = obs

    def length(self):
        n, k = [int(self.n), int(self.k)]
        rQueen, cQueen = {int(self.rQueen), int(cQueen)}


        # north
        move = 0
        r = rQueen
        c = cQueen
        while (r < n):
            if [r + 1, c] in self.obstacle:
                break
            else:
                move += 1
                r += 1

        # north east
        r = rQueen
        c = cQueen
        while (r < n and c < n):
            if [r + 1, c + 1] in self.obstacle:
                break
            else:
                move += 1
                r += 1
                c += 1

        # east
        r = rQueen
        c = cQueen
        while (c < n):
            if [r, c + 1] in self.obstacle:
                break
            else:
                move += 1
                c += 1

        # south west
        r = rQueen
        c = cQueen
        while (r > 1 and c < n):
            if [r - 1, c + 1] in self.obstacle:
                break
            else:
                move += 1
                r -= 1
                c += 1

        # south
        r = rQueen
        c = cQueen
        while (r > 1):
            if [r - 1, c] in self.obstacle:
                break
            else:
                move += 1
                r -= 1

        # south west
        r = rQueen
        c = cQueen
        while (r > 1 and c > 1):
            if [r - 1, c - 1] in self.obstacle:
                break
            else:
                move += 1
                r -= 1
                c -= 1

        # west
        r = rQueen
        c = cQueen
        while (c > 1):
            if [r, c - 1] in self.obstacle:
                break
            else:
                move += 1
                c -= 1

        # north west
        # south
        r = rQueen
        c = cQueen
        while (r < n and c > 1):
            if [r + 1, c - 1] in self.obstacle:
                break
            else:
                move += 1
                r += 1
                c -= 1


def main():


if __name__ == '__main__':
    main()

