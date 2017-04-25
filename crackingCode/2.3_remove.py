class Node:
    def __init__(self,item):
        self.val=item
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
        cur =self.head
        result =[]
        while cur is not None:
            result.append(cur.val)
            cur=cur.next
        return result

    def remove(self,item): #Three cases 1) first node 2)in between node 3)last node
        if self.head.val == item: #1)first node
            self.head = self.head.next
            return
        else :
            cur=self.head
            while cur.next is not None:
                if cur.val==item: #2) in between node
                    self.removeItem(item)
                    return

                if (cur.next.next is None) and cur.next.val == item: #3)last node
                    cur.next= None
                    return
                cur=cur.next
            print('item does not exist in linked list')

    def removeItem(self,item):
        cur=self.head
        while cur.next is not None:
            if cur.next.val ==item:
                nextnode= cur.next.next
                cur.next= nextnode
                break
            cur=cur.next

ll = LinkedList(9)
ll.add(5)
ll.add(8)
ll.add(7)
ll.add(6)
# print(ll.printlist())
ll.remove(7)
print(ll.printlist())
