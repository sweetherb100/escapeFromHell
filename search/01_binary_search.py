'''
*binary search
1) should be sorted in advance
2) start, end, middle should be the index
3) while should be start <= end
4) middle should have int(): should not be float!
'''

def binary_search(list, target):
    start=0
    end=len(list)-1

    while start <= end : #stop when end < start
        middle = (start + end) // 2 #update middle

        if target == list[middle]:
            return True

        elif target < list[middle]: #on the left
            end = middle-1 #update end


        elif list[middle] < target:
            start = middle+1 #update start

    return False



print(binary_search([1,2,3,4,5,6,7], 7))