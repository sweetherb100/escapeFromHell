'''
Time Complexity : O(n)
Space Complexity : O(n)

*remove duplicate Outline :
1) use Dictionary (Hash)
2) use prev Node (to link with previous and next node)
'''


class Node:
    def __init__(self,item):
        self.val=item
        self.next=None #pointer (reference)

class LinkedList:
    def __init__(self,item):
        self.head = Node(item)

    def add(self,item):
        cur=self.head #it is not value but Node itself (pointer)
        while cur.next is not None: #when cur.next is None, stop (plays role just to move to the end)
            cur=cur.next
        cur.next = Node(item)

    def printlist(self):
        cur=self.head
        res=[]
        while cur is not None:
            res.append(cur.val)
            cur=cur.next
        return res

    def delete_duplicate (self):
        cur = self.head
        dict ={}
        prev =None # pointer; pointing the same as cur

        # prev is the the result of copy by reference to the cur
        # it is "prev=cur", not "pre=cur.val"
        while cur is not None:
            if cur.val in dict: #exist duplicate
                prev.next=cur.next
            else : #doesn't exist duplicate
                dict[cur.val]=True
                prev = cur

            cur = cur.next

ll=LinkedList(3)
ll.add(4)
ll.add(5)
ll.add(6)
ll.add(4)
ll.add(7)
ll.add(4)
ll.add(6)
ll.add(6)
print(ll.printlist())
ll.delete_duplicate()
print(ll.printlist())
