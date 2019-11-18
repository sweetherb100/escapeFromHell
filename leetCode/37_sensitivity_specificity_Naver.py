# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
# https://en.wikipedia.org/wiki/Sensitivity_and_specificity


def solution(A, B, q):
    # assumption: length of array >=1
    # focus on correctness!!

    # Exception
    if len(A) != len(B):
        return -1  # wrong data input

    TP = 0
    FN = 0
    FP = 0
    TN = 0

    for i in range(len(A)):
        if A[i] == 1 and B[i] == 1:
            TP += 1
        elif A[i] == 1 and B[i] == 0:
            FN += 1
        elif A[i] == 0 and B[i] == 1:
            FP += 1
        elif A[i] == 0 and B[i] == 0:
            TN += 1

    if q == False:  # sensitivity = TP/(TP+FN)
        return TP / (TP + FN)
    elif q == True:  # specificity = TN/(TN+FP)
        return TN / (TN + FP)


