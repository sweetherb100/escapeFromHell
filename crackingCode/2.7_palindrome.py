'''
*Question : palindrome (if string and reversed string are the same)
(linkedlist reverse question)
cf) anagram : if two strings are permutation to each other

*Idea : 
Between 2 linkedlist, reverse one and check whether it is the same
'''

class Node:
    def __init__(self,item):
        self.val =item
        self.next=None

class LinkedList:
    def __init__(self,item):
        self.head = Node(item)

    def add(self,item):
        cur=self.head
        while cur.next is not None:
            cur=cur.next
        cur.next=Node(item)

    def printlist(self):
        cur=self.head
        result=[]
        while cur is not None:
            result.append(cur.val)
            cur=cur.next
        return result

    def reverse(self):
        cur=self.head
        prev=None
        while cur is not None:
            next=cur.next
            cur.next=prev
            prev=cur
            cur=next
        self.head=prev #reset self.head

def solution(list):
    input=list.printlist()
    list.reverse()
    output=list.printlist()
    if input==output:
        return True
    else:
        return False

list1 = LinkedList(1)
list1.add(3)
list1.add(5)
list1.add(3)
list1.add(1)

list2 = LinkedList(5)
list2.add(9)
list2.add(2)

print(solution(list1))
print(solution(list2))

