# We'd love to hear your feedback about one of the tasks you've just solved: "Create a k-fold sampler function."
# Create a k-fold sampler function.

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")


##### ONLY 50% CORRECT....
def solution(indices, K):
    # Exception1: K shouldn't bigger than the length of array
    if len(indices) < K:
        return []


    result = []
    if len(indices) % K == 0:  # can evenly divided
        div = len(indices)//K
        for iter in range(K):
            test = indices[iter * div:(iter + 1) * div]
            train=[]
            for i in range(len(indices)):
                if indices[i] not in test:
                    train.append(indices[i])
            result.append(train)
            result.append(test)

    else: #len(indices)%K != 0: cannot evenly divide
        div = len(indices)//K+1 #add + 1
        if len(indices)%div == 0: #if new divisor is divisible, don't add +1
            div = len(indices)//K

        ##### The sizes of the pairs of testing sets may differ by no more than 1 ####
        for iter in range(K):
            remained = len(indices) - (K - 2) * div  # last 2 remaining testing sets
            lastfoldlen = len(indices) - (K - 1) * div

            if iter <K-2:
                test = indices[iter * div:(iter + 1) * div]
            else : #when iter == K-2 or K-1
                if div- lastfoldlen > 1:  # The sizes of the pairs of testing sets may differ by no more than 1
                    if iter == K-2:
                        test = indices[iter * div:iter*div + remained//2]
                    if iter == K-1: #reached the end
                        test = indices[(iter-1)*div + remained//2:] #take the rest as whole test set
                else :
                    if iter == K-2:
                        test = indices[iter * div:(iter + 1) * div] #use the original
                    if iter == K-1: #reached the end
                        test = indices[iter * div:] #take the rest as whole test set

            train = []
            for i in range(len(indices)):
                if indices[i] not in test:
                    train.append(indices[i])
            result.append(train)
            result.append(test)

    return result

# ([1,2,3,4,5,6,7,8,9,10],5)
# ([1,2,3,4,5,6,7,8,9,10],4)
# ([1,2,3,4,5,6,7,8,9,10],3)
# ([1,2,3,4,5,6,7,8,9,10],2)
#
#
# ([1,2,3,4,5,6,7,8,9],5)
# ([1,2,3,4,5,6,7,8,9],4)
# ([1,2,3,4,5,6,7,8,9],3)
# ([1,2,3,4,5,6,7,8,9],2)
