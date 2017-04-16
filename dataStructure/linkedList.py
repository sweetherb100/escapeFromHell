# linkedList : 기본적으로 node들이 linked된 data structure
# 특징 1) Node 클래스, LinkedList 클래스 만들어주기
# 2) head 값 별도로 저장. ex) cur = self.head

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
            #while문을 통해 linkedList 끝으로 간다.
        cur.next=Node(item)

    def remove(self,item):
        #3가지 경우 : remove 대상이 head 일때 / 사이에 있을 때 / 맨 마지막 Node일 때
        if self.head.val == item: #1)remove 대상이 head 일때
            self.head = self.head.next
        else : #2) 사이에 있을 때
            cur=self.head
            while cur.next is not None:
                if cur.val ==item:
                    self.removeItem(item)
                    return

                if (cur.next.next is None) and cur.next.val == item: #3) 마지막 Node일 때 (previous를 알아야 된다)
                    cur.next=None
                    return
                cur=cur.next

            print("item does not exist in linked list")

    def removeItem(self,item):
        cur=self.head
        while cur.next.next is not None:
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
        self.head = prev #head 다시 재설정

    def printlist(self):
        cur =self.head
        while cur is not None:
            print(cur.val)
            cur=cur.next

# linkedlist = LinkedList() #이렇게 쓰면 안됨
linkedlist = LinkedList(1)
linkedlist.add(2)
linkedlist.add(3)
linkedlist.add(4)
linkedlist.remove(3)
linkedlist.printlist()
print('********************')
linkedlist.reverse()
linkedlist.printlist()

#참고사이트
#https://github.com/minsuk-heo/problemsolving/blob/master/data_structure/Stack.py