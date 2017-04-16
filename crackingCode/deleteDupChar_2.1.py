# Time Complexity : O(n)
# Space Complexity : O(n)
#
# 기본아이디어 :
# 1) Dictionary 사용 (Hash)
# 2) 이전 Node와 다음 Node 연결해야되니까 prev Node 개념 있어야

#LinkedList 나오면
# 1) Node Class 선언 (self.val, self.next)
# 2) LinkedList Class 선언 (self.head)
# 3) LinkedList Class 중 __init__, add, printlist 메소드 선언

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
        prev =None

        while cur is not None:
            if cur.val in dict:
                prev.next=cur.next
            else :
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
ll.delete_duplicate()
print(ll.printlist())
