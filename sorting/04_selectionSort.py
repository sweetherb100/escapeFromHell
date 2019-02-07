'''
Worst case performance : O(n^2)
Best case performance : O(n^2)
Average case performance : O(n^2)
Worst case space complexity : O(n), O(1) auxiliary (=Minimum value)
'''
def selectionSort(input):
    for i in range(len(input)-1) : #skip the last element(will automatically be the largest)
        idx_min = i
        j=i+1

        while j<len(input):
            if(input[j]<input[idx_min]):
                idx_min = j
            j=j+1

        if idx_min is not i:
            input[idx_min],input[i] = input[i], input[idx_min]

    return input

print(selectionSort([4,6,1,3,5,2,0,3523,1,326]))