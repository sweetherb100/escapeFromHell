# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(X, Y):
    # write your code in Python 3.6
    # Let's think about the exception case later
    sum = 0

    # assuming that the length is the same
    for i in range(1, len(X), 1):  # starting from one after
        trapezoid = ((Y[i - 1] + Y[i]) / 2) * (X[i] - X[i - 1])
        sum += trapezoid

    return sum

