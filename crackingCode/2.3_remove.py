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

    def remove(self,item): #경우 3가지 remove 대상이 1)첫번째 node일 때 2)중간 노드일 때 3)마지막 노드일 때
        if self.head.val == item: #1)첫번째 node일 때
            self.head = self.head.next
            return
        else :
            cur=self.head
            while cur.next is not None:
                if cur.val==item: #2) 중간 노드일 때
                    self.removeItem(item)
                    return

                if (cur.next.next is None) and cur.next.val == item: #3)마지막 노드일 때
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
