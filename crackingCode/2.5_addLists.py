'''
*Question : Add two numbers represented by linkedlist and return int result value 

*Python :
1) def outside of class : inside def, initialize class (cannot use self)
2) (v1.val+v2.val) //10 : divide

*LinkedList Tip :
1) Make getHead method(return self.head) to be used outside of class
'''


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
        # val = ((v1.val+v2.val)%10) + carry #way1 #this can return 10 and it is okay
        val = ((v1.val + v2.val+carry) % 10)  #way2
        # 9 - 8 - 2
        # 1 - 1 - 3
       #c 0 - 1 - 0
        # result :
        # 0 + 0 + 6 (600) (X)
        # 0 + 10 + 5 (600) (O)
        # Misunderstanding : doesn't return String but int. So doesn't have to return val into unit's digit
        # ex)carry : 0, val : 10 is okay

        # carry =(v1.val+v2.val) //10  #way1
        carry = (v1.val + v2.val+carry) // 10 #way2
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
    #return int (dont need to use string append)
    while cur is not None:
        val=val+(cur.val*mul)
        mul=mul*10
        cur=cur.next
    return val


list1 = LinkedList(7) #7-1-7
list1.add(1)
list1.add(7)

list2 = LinkedList(5) #5-9-2-3
list2.add(9)
list2.add(2)
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
