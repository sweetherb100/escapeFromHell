# Given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.
#
# For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.
# Given A = [1, 2, 3], the function should return 4.
# Given A = [−1, −3], the function should return 1.
#
# Write an efficient algorithm for the following assumptions:
# N is an integer within the range [1..100,000];
# each element of array A is an integer within the range [−1,000,000..1,000,000].

# 1. MissingInteger (level: medium)
# Find the smallest positive integer that does not occur in a given sequence.

### tip:
# 1) I can use sorting!
# 2) I can use while clause!
# 3) if there is index+1, then be careful with the while condition!

# my strategy: if I find 1, I go on and see if there is missing values. If I reached the end, i return the next number
# if I don't find 1, that is the smallest value

def solution(A):
    # cases
    # if all negative: 1
    # if all consecutive : next number
    # if a missing positive value : that missing positive value

    # Exception
    if len(A) == 0:
        return -1   # array is empty

    A.sort()

    if 1 not in A: #there is no 1 in the array => it becomes the smallest positive value
        return 1

    index = 0
    while (index < len(A)-1): #stop when index == the end
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
