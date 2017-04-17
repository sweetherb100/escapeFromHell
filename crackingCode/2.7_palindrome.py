#palindrome : 앞에서부터 읽을 때와 뒤에서부터 읽을때 같을 경우
#cf) anagram : 2개의 string이 서로 순열관계인지. (문자열 바꿔서 서로 같으면 TRUE)
#기본 아이디어 : linkedlist 2개 중 하나를 reverse 시켜서 서로 같으면 TRUE
# ***linkedlist reverse 문제

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
        self.head=prev #head 다시 재설정

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

