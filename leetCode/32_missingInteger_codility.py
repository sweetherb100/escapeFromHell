# This is a demo task.

# Write a function:
# def solution(A)
# that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.
#
# For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.
# Given A = [1, 2, 3], the function should return 4.
# Given A = [−1, −3], the function should return 1.
#
# Write an efficient algorithm for the following assumptions:
# N is an integer within the range [1..100,000];
# each element of array A is an integer within the range [−1,000,000..1,000,000].

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

# 1. MissingInteger (level: medium)
# Find the smallest positive integer that does not occur in a given sequence.

### tip:
# 1) I can use sorting!
# 2) I can use while clause!
# 3) if there is index+1, then be careful with the while condition!

def solution(A):
    # write your code in Python 3.6
    # cases
    # if all negative: 1
    # if all consecutive : next number
    # if a missing positive value : that missing positive value

    # my strategy: if I find 1, I go on and see if there is missing values. If I reached the end, i return the next number
    # if I don't find 1, that is the smallest value

    # Exception
    if len(A) == 0:
        return -1   # array is empty

    A.sort()

    if 1 in A:
        index = A.index(1)
    else: #there is no 1 in the array => it becomes the smallest positive value
        return 1


    while (index < len(A)-1):
       if A[index] + 1 < A[index+1] :
           return A[index] + 1
       index+=1

    return A[index] + 1

print(solution([1, 3, 6, 4, 1, 2])) #5
print(solution([1, 2, 3])) #4
print(solution([-1, -3])) #1

print(solution([4])) #1
print(solution([])) #False
print(solution([-1, 5])) #1
print(solution([0])) #1
print(solution([5, 4, 3, 2, -1])) #1

# Compilation successful.
#
# Example test:   [1, 3, 6, 4, 1, 2]
# OK
#
# Example test:   [1, 2, 3]
# OK
#
# Example test:   [-1, -3]
# OK
#
# Your code is syntactically correct and works properly on the example test.
# Note that the example tests are not part of your score. On submission at least 8 test cases not shown here will assess your solution.