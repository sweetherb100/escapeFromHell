'''
*Question : partition a linked list given a pivot value
put smaller element than pivot to left, bigger element than pivot to right 
(Eventually make one linkedlist not divided linkedlists?)

*Idea :
1) Make pre, post 2 linkedlist and traverse
(Partition : just make two linkedlist)
2) then connect pre, pivot value, post linkedlist

*LinkedList Tip :
1) Make getHead method(return self.head) to be used outside of class
2) After cur = pre.getHead() and moving cur to the end and connect sth, 
 eventually pre linkedlist will have different form and pre.getHead() still returns the head regardless of cur 
 
*Python :
1) def outside of class : inside def, initialize class (cannot use self)
'''

class Node:
    def __init__(self,item):
        self.val=item
        self.next=None

class LinkedList:
    def __init__(self,item):
        self.head=Node(item)

    def add(self,item):
        cur = self.head
        while cur.next is not None:
            cur=cur.next
        cur.next=Node(item)

    def printlist(self):
        cur =self.head
        result=[]
        while cur is not None:
            result.append(cur.val)
            cur=cur.next
        return result

    def getHead(self):
        return self.head

#def outside of class : inside def, initialize class (cannot use self)
def solution(ll,key):
    cur=ll.getHead()
    pre=None
    post=None
    while cur is not None:
        if cur.val != key:
            if key < cur.val:
                if post is None:
                    post=LinkedList(cur.val) #initialize
                else:
                    post.add(cur.val)
            elif cur.val < key:
                if pre is None:
                    pre=LinkedList(cur.val) #initialize
                else:
                    pre.add(cur.val)
        cur=cur.next

    # connect pre, pivot value, post linkedlist
    cur=pre.getHead()
    while cur.next is not None:
        cur=cur.next
    cur.next=Node(key)
    cur.next.next=post.getHead()
    return pre.printlist()

ll = LinkedList(6)
ll.add(3)
ll.add(8)
ll.add(1)
ll.add(5)
ll.add(9)
print(ll.printlist())
print(solution(ll,5))

