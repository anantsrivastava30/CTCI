from sympy.physics.quantum.circuitplot import np

# CTCI problem tells if two words are rotation invariant
# example "hello world" and "world hello"

def compressor(srr):
    c = srr[0]
    checker = c
    flag = False
    num = 1
    for word in srr[1:]:
        x = word
        if x == c:
            num += 1
            flag = True
        else:
            checker += str(num)
            num = 1
            checker += x
        c = word
    if flag is False:
        return srr
    else:
        return checker


def transpose(A):
    m,n = A.shape
    for layer in range(int(n/2)):
        first = layer
        last = n-1-layer
        for i in range(first, last):
            offset = i-first
            top = A[first][i]
            A[first][i] = A[last - offset][first]
            A[last - offset][first] = A[last][last - offset]
            A[last][last - offset] = A[i][last]
            A[i][last] = top

    print(A)


# 1.7
def nullrow(A, row):
    A[row, :] = 0


# 1.7
def nullcol(A, col):
    A[:, col] = 0

# 1.7
def zeroforzero(A):
    m,n = A.shape
    row = np.zeros(m)
    col = np.zeros(n)
    for i in range(m):
        for j in range(n):
            if A[i][j] == 0:
                row[i] = 1
                col[j] = 1

    for i in range(m):
        if row[i] == 1:
            nullrow(A, i)

    for i in range(n):
        if col[i] == 1:
            nullcol(A, i)

    print(A)


# 1.8
def isRotation(str1, str2):
    l1 = len(str1)
    l2 = len(str2)
    if l1 == l2 and l1 and l2 > 0:
        temp = str1+str1
        if str2 in temp:
            return True
        else:
            return False
    else:
        return False



def main():
    str = "helloworld"
    str1 = "worldhello"
    print(compressor(str))
    # A = np.array([[1,2,3,4],[0,5,6,4],[7,8,9,7]])
    # zeroforzero(A)
    # transpose(A)
    print(isRotation(str, str1))


if __name__ == "__main__":
    main()
