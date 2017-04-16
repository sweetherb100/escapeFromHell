def insertionSort(input):
    for idx,valueToInsert in enumerate(input):
        holePosition = idx

        while holePosition > 0 and input[holePosition-1] > valueToInsert:
            #holePosition > 0을 통해 holePosition ==0일때 제외
            input[holePosition-1],input[holePosition] = input[holePosition], input[holePosition-1]
            holePosition = holePosition -1

    return input

print(insertionSort([4, 6, 1, 3, 5, 2]))

#참고
# list =[1, 2, 3, 4, 5, 6]
# print(list[-1])
# 뒤에서 첫번째 index