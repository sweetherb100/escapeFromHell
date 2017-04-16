#partition a linked list given a pivot value
# pivot value 기준으로 작은 값은 pivot 왼쪽, 큰 값은 pivot 오른쪽
# 기본 아이디어 : pre, post 2개의 linkedlist를 만들어서 순회하기

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

#LinkedList class 밖에 있어야 하는 메소드. 따라서 self의 개념이 없다.
def solution(ll,key):
    cur=ll.getHead()
    pre=None
    post=None
    while cur is not None:
        if cur.val != key:
            if cur.val > key:
                if post is None:
                    post=LinkedList(cur.val)
                else:
                    post.add(cur.val)
            elif cur.val <key:
                if pre is None:
                    pre=LinkedList(cur.val)
                else:
                    pre.add(cur.val)
        cur=cur.next

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

