'''
*LinkedList
1) data structure linked with Nodes
2) create Node class, LinkedList class
3) [tip] save head (don't use directly) ex) cur = self.head
4) [initialize] linkedlist = LinkedList(1) (linkedlist = LinkedList() (X))
5) remove method : 
5-1) the target is self.head
5-2) the target is in between
5-3) the target is in the end
'''

class Node:
    def __init__(self,item):
        self.val = item
        self.next = None

class LinkedList:
    def __init__(self,item):
        self.head=Node(item)

    def add(self,item):
        cur=self.head
        while cur.next is not None:
            cur=cur.next
        cur.next=Node(item)

    def remove(self,item): #3 cases
        if self.head.val == item: #1)the target is self.head
            self.head = self.head.next
        else : #2) the target is in between
            cur=self.head
            while cur.next is not None:
                if cur.val ==item:
                    self.removeItem(item)
                    return

                if (cur.next.next is None) and cur.next.val == item: #the target is in the end
                    cur.next=None
                    return
                cur=cur.next
            print("item does not exist in linked list")

    def removeItem(self,item):
        cur=self.head
        while cur.next.next is not None: #link with the next.next node
            if cur.next.val == item:
                nextnode = cur.next.next
                cur.next = nextnode
                break
            cur=cur.next

    def reverse(self):
        cur = self.head
        prev = None
        while cur is not None:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
        self.head = prev #reset the head of reversed linkedlist

    def printlist(self):
        cur =self.head
        while cur is not None:
            print(cur.val)
            cur=cur.next

# linkedlist = LinkedList() #wrong
linkedlist = LinkedList(1)
linkedlist.add(2)
linkedlist.add(3)
linkedlist.add(4)
linkedlist.remove(3)
linkedlist.printlist()
print('********************')
linkedlist.reverse()
linkedlist.printlist()
