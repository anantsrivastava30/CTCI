A = [5,1,3]
X = 8
D = 2


def solution(A, X, D):
    n = len(A)

    if X <= D:
        return 0
        
    if n == 0:
        return -1
        
    if A[0] <= D:
        if X <= D + A[0]:
            return 0

    leaves = [0 for x in range(X)]

    curr = 0
    for i in range(n):
        leaves[A[i]] = 1
        if A[i] - curr <= D and A[i] - curr > 0:
            curr = A[i]
            for x in range(len(leaves[curr:])):
                if leaves[x] == 1 and x <= D:
                    curr += x

        if X - curr <= D:
            return i
    print(leaves)
    return -1

print(solution(A,X,D))