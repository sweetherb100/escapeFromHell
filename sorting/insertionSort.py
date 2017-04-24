'''
best case performance : O(n)
worst case performance : O(n^2)

*Python
1) range(biggest, smallest-1,-1) : reverse range
ex) for i in range(10,-1, -1) :
'''

#way 1
def insertionSort(input):
    for idx,valueToInsert in enumerate(input):
        holePosition = idx
        while holePosition > 0 and input[holePosition-1] > valueToInsert:
            #exclude holePostition == 0
            input[holePosition-1],input[holePosition] = input[holePosition], input[holePosition-1]
            holePosition = holePosition -1

    return input

#way2
    # for i in range(1,len(alist)): #exclude the first index
    #     for j in range(i,0,-1) :
    #         if alist[j] < alist[j-1] :
    #             alist[j], alist[j-1] = alist[j-1],alist[j]
    #         else:
    #             break
print(insertionSort([4, 6, 1, 3, 5, 2]))