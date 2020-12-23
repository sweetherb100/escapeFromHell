def RMSE(predicted, observed):
    mse = 0
    tol = pow(10, -4)

    # Exception: if the length doesn't match, it is wrong
    if len(predicted) != len(observed):
        return -1  # cannot be accepted

    sum = 0
    for i in range(len(predicted)):
        sum += pow(float(predicted[i] - observed[i]),2) #square

    mse = pow(sum/len(predicted), 0.5) #root squared
    return mse

print(RMSE([4, 25,  0.75, 11], [3, 21, -1.25, 13]))
print(RMSE([1.111, 2.111, 3.111], [1.0, 2.0, 3.0]))