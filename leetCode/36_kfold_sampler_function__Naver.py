# We'd love to hear your feedback about one of the tasks you've just solved: "Create a k-fold sampler function."
# Create a k-fold sampler function.

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

#strategy: when K is not evenly divided, take care of the 'rest test candidate' by updating 'K' and 'rest test candidate'

def solution(indices, K):
    # Exception1: K shouldn't bigger than the length of array
    if len(indices) < K:
        return []


    result = []
    if len(indices) % K == 0:  # can evenly divided
        div = len(indices)//K
        for iter in range(K):
            test = indices[iter * div:(iter + 1) * div]
            train = [elem for elem in indices if elem not in test]
            result.append(train)
            result.append(test)


    else: #cannot evenly divide
        test_rest = indices
        while (len(test_rest) > 0): #stop when length==0
            if len(test_rest) % K == 0:
                div = len(test_rest) // K #be careful to update test_rest, not indices!
            else:
                div = len(test_rest) // K + 1  # add + 1

            test = test_rest[0:div]
            train = [elem for elem in indices if elem not in test]
            result.append(train)
            result.append(test)

            #update
            test_rest = test_rest[div:len(test_rest)]
            K=K-1

    return result

print(solution([1,2,3,4,5,6,7,8,9,10],5))
print(solution([1,2,3,4,5,6,7,8,9,10],4)) #10/4=2.5 (10-3)/3=2.XX
print(solution([1,2,3,4,5,6,7,8,9,10],3)) #10/3=3.3
print(solution([1,2,3,4,5,6,7,8,9,10],2)) #10/2=5

print(solution([1,2,3,4,5,6,7,8,9],5)) #9/5=1.8
print(solution([1,2,3,4,5,6,7,8,9],4)) #9/4=2.25 => (9-3)/3=2
print(solution([1,2,3,4,5,6,7,8,9],3)) #9/3=3
print(solution([1,2,3,4,5,6,7,8,9],2)) #9/2=4.5

##### ONLY 50% CORRECT....
# def solution2(indices, K):
#     # Exception1: K shouldn't bigger than the length of array
#     if len(indices) < K:
#         return []
#
#
#     result = []
#     if len(indices) % K == 0:  # can evenly divided
#         div = len(indices)//K
#         for iter in range(K):
#             test = indices[iter * div:(iter + 1) * div]
#             train=[]
#             for i in range(len(indices)):
#                 if indices[i] not in test:
#                     train.append(indices[i])
#             result.append(train)
#             result.append(test)
#
#     else: #len(indices)%K != 0: cannot evenly divide
#         div = len(indices)//K+1 #add + 1
#         if len(indices)%div == 0: #if new divisor is divisible, don't add +1
#             div = len(indices)//K
#
#         ##### The sizes of the pairs of testing sets may differ by no more than 1 ####
#         for iter in range(K):
#             remained = len(indices) - (K - 2) * div  # last 2 remaining testing sets
#             lastfoldlen = len(indices) - (K - 1) * div
#
#             if iter <K-2:
#                 test = indices[iter * div:(iter + 1) * div]
#             else : #when iter == K-2 or K-1
#                 if div- lastfoldlen > 1:  # The sizes of the pairs of testing sets may differ by no more than 1
#                     if iter == K-2:
#                         test = indices[iter * div:iter*div + remained//2]
#                     if iter == K-1: #reached the end
#                         test = indices[(iter-1)*div + remained//2:] #take the rest as whole test set
#                 else :
#                     if iter == K-2:
#                         test = indices[iter * div:(iter + 1) * div] #use the original
#                     if iter == K-1: #reached the end
#                         test = indices[iter * div:] #take the rest as whole test set
#
#             train = []
#             for i in range(len(indices)):
#                 if indices[i] not in test:
#                     train.append(indices[i])
#             result.append(train)
#             result.append(test)
#
#     return result
#
# print(solution2([1,2,3,4,5,6,7,8,9,10],5))
# print(solution2([1,2,3,4,5,6,7,8,9,10],4)) #10/4=2.5 (10-3)/3=2.XX
# print(solution2([1,2,3,4,5,6,7,8,9,10],3)) #10/3=3.3
# print(solution2([1,2,3,4,5,6,7,8,9,10],2)) #10/2=5
#
# print(solution2([1,2,3,4,5,6,7,8,9],5)) #9/5=1.8
# print(solution2([1,2,3,4,5,6,7,8,9],4)) #9/4=2.25 => (9-3)/3=2
# print(solution2([1,2,3,4,5,6,7,8,9],3)) #9/3=3
# print(solution2([1,2,3,4,5,6,7,8,9],2)) #9/2=4.5
