def solution(predicted, observed):
    # write your code in Python 3.6
    mse = 0
    tol = pow(10, -4)

    # Exception: if the length doesn't match, it is wrog
    if len(predicted) != len(observed):
        return -1  # cannot be accepted

    sum = 0
    for i in range(len(predicted)):
        #print(float(predicted[i] - observed[i]))
        sum += pow(float(predicted[i] - observed[i]),2)

    mse = pow(sum/len(predicted), 0.5)
    return mse

print(solution([4, 25,  0.75, 11], [3, 21, -1.25, 13]))
print(solution([1.111, 2.111, 3.111], [1.0, 2.0, 3.0]))
# [1.111, 2.111, 3.111], [1.0, 2.0, 3.0]