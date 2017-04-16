# Add two numbers represented by linkedlist and return int result value

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

    def getHead(self):
        return self.head


def solution(list1, list2):
    v1=list1.getHead()
    v2=list2.getHead()
    carry =0
    while v1 is not None and v2 is not None:
        val = ((v1.val+v2.val)%10) + carry #이것까지 더해서 10이될수있지않을까?
        # 9 - 8 - 2
        # 1 - 1 - 3
        # result :
        # 0 + 0 + 6 (600) (X)
        # 0 + 10 + 5 (600) (O)
        # 내가 오해했던 부분 : string으로 처리하는게 아니라 어차피 int로 추후 변환할것이기 때문에
        # 꼭 1의 자리수가 맞추어져서 나올 필요없다.
        # ex)carry : 0, val : 10으로 나와도 괜춘

        carry =(v1.val+v2.val) //10
        # print('carry : ',carry)
        # print('val : ',val)
        v1.val = val
        v1=v1.next
        v2=v2.next

    while v1 is not None:
        v1.val=v1.val+carry
        carry=0
        v1=v1.next

    while v2 is not None:
        list1.add(v2.val+carry)
        carry=0
        v2=v2.next

    cur=list1.getHead()
    val=0
    mul=1
    #return int result.(그래서 string append 대신에 int값으로 만들어줘서 return)
    while cur is not None:
        val=val+(cur.val*mul)
        mul=mul*10
        cur=cur.next
    return val


list1 = LinkedList(7)
list1.add(1)
list1.add(7) #1012
# list1.add(5)

list2 = LinkedList(5)
list2.add(9)
list2.add(2) #1012
list2.add(3)

print(solution(list1,list2))


# list1 = LinkedList(9)
# list1.add(8)
# list1.add(2)
#
# list2 = LinkedList(1)
# list2.add(1)
# list2.add(3)
#
# print(solution(list1,list2))