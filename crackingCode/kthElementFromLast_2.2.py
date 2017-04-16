# 기본 아이디어  : 2개의 포인터 사용
# Step 1: kth 만큼 2번째 포인터 옮기기
# Step 2: 2번째 포인터.next가 null일 때까지 1번째 포인터와 2번째 포인터 같이 옮기기
# Step 3: 1번째 포인터가 가르키는 값이 끝에서 n번째 값

class Node:
    def __init__(self,item):
        self.val = item
        self.next=None

class LinkedList:
    def __init__(self,item):
        self.head = Node(item)

    def add(self,item):
        cur =self.head
        while cur.next is not None:
            cur=cur.next
        cur.next=Node(item)

    def printlist(self):
        cur=self.head
        res = []
        while cur is not None:
            res.append(cur.val)
            cur=cur.next
        return str(res)

    def kth_element_from_last(self,k):
        p1=self.head
        p2=self.head
        if k!=0:
            for i in range(k): #k만큼 for loop을 돈다
                p2=p2.next
                #over flow k is greater than linkedlist length
                if p2 is None:
                    return None
        #run until p2 reach the end
        while p2.next is not None:
            p2=p2.next
            p1=p1.next
        #since p2-p1 is the k, now p1 position is kth from the last node
        return p1.val

ll = LinkedList(3)
ll.add(4)
ll.add(5)
ll.add(6)
ll.add(4)
ll.add(7)
ll.add(4)
print(ll.printlist())
print(ll.kth_element_from_last(2))
