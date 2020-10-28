# https://en.wikipedia.org/wiki/Freivalds%27_algorithm

def cipher(n, m, k, firstmat, secondmat, thirdmat):
    candZ = getCandidateZ(n, m, k, thirdmat)
    print(candZ)
    randomvecs = getRandVectors([], k)  # takes too much time for recursion

    for tri in range(len(randomvecs)):
        randomvec = randomvecs[tri]
        print(randomvec)

        candilen = len(candZ)  # number of candidate matrix, measure the length every iteration
        for candindx in range(candilen - 1, -1, -1):  # start from the back because I will pop in below
            Bmatrix = candZ[candindx]

            Br = matrixvecmult(Bmatrix, randomvec)
            ABr = matrixvecmult(firstmat, Br)
            Cr = matrixvecmult(secondmat, randomvec)
            minusvec = [x - y for x, y in zip(ABr, Cr)]

            for i in range(k):
                if minusvec[i] != 0:
                    candZ.pop(candindx)  # the right matrix should ALWAYS be zero vector
                    break

    return len(candZ)


def matrixvecmult(matrix, list):
    vector = []
    for i in range(len(list)):
        mult = [x * y for x, y in zip(matrix[i], list)]
        vector.append(sum(mult))
    return vector


def getCandidateZ(n, m, k, thirdmat):
    result = []
    temp = []
    for j in range(0, m - k + 1, 1):
        for i in range(0, n - k + 1, 1):
            temp = []
            for ii in range(i, i + k, 1):
                temp.append(thirdmat[ii][j:j + k])

            result.append(temp)
    return result


# logic: recursion
def getRandVectors(randvecs, k):
    subvec = [0] * k  # to be updated as recursion (just need to overwrite on top)
    vector_helper(randvecs, subvec, k, 0)
    return randvecs


def vector_helper(randvecs, subvec, k, cur):
    # base condition : reached the end
    if cur == k:
        randvecs.append(subvec[::])  # copy by value the list
        return

    # 2 recursion
    subvec[cur] = 0
    vector_helper(randvecs, subvec, k, cur + 1)  # go for the next index
    subvec[cur] = 1
    vector_helper(randvecs, subvec, k, cur + 1)  # go for the next index


# Enter your code here. Read input from STDIN. Print output to STDOUT
# casecnt = int(input())
# for i in range(casecnt):
#     nmk = [int(part) for part in input().split()]  # input as int element array
#     n = nmk[0]
#     m = nmk[1]
#     k = nmk[2]
#
#     firstmat = []
#     secondmat = []
#     thirdmat = []
#     for i in range(k):
#         firstmat.append([int(part) for part in input().split()])
#     for i in range(k):
#         secondmat.append([int(part) for part in input().split()])
#     for i in range(n):
#         thirdmat.append([int(part) for part in input().split()])

n=3
m=4
k=2
firstmat=[[1,0],[0,1]]
secondmat=[[1,1],[0,1]]
thirdmat = [[1,1,1,1], [0,1,0,1], [1,3,1,-1]]
print(cipher(n, m, k, firstmat, secondmat, thirdmat)) #2

n=1
m=4
k=1
firstmat= [[2]]
secondmat= [[6]]
thirdmat = [[3,4,3,3]]
print(cipher(n, m, k, firstmat, secondmat, thirdmat)) #3