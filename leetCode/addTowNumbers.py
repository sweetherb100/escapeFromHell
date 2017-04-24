'''
Question:
You are given two non-empty linked lists representing two non-negative integers. 
The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8

Outline :
1) linkedList : Consists of Node

TestCase:
1) l1=[5], l2=[5]
2) l1 is longer (or l2 is longer)

'''

class Node:
    def __init__(self,item):
        self.val = item
        self.next= None

class linkedList:
    def __init__(self,item):
        self.head = Node(item)

    def add(self,item):
        cur=self.head
        while cur.next is not None:
            cur=cur.next
        cur.next=Node(item)

    def printLinkedList(self):
        cur=self.head
        result=[]
        while cur is not None:
            result.append(cur.val)
            cur=cur.next
        return result

class Solution():
    def addTwoNumbers(self,l1,l2):
        cur1 = l1.head
        cur2 = l2.head
        carry = 0
        result=linkedList((cur1.val+cur2.val+carry)%10)
        carry = (cur1.val + cur2.val + carry) // 10
        cur1=cur1.next
        cur2=cur2.next

        while cur1 is not None and cur2 is not None:
            result.add((cur1.val+cur2.val+carry)%10)
            carry=(cur1.val+cur2.val+carry)//10
            cur1=cur1.next
            cur2=cur2.next

        while cur1 is not None:
            result.add((cur1.val + carry) % 10)
            carry = (cur1.val + carry) // 10
            cur1 = cur1.next

        while cur2 is not None:
            result.add((cur2.val + carry) % 10)
            carry = (cur2.val + carry) // 10
            cur2 = cur2.next

        if carry == 1:
            result.add(carry)

        return result.printLinkedList()



sol = Solution()
# l1=linkedList()
l1=linkedList(5)
# l1.add(4)
# l1.add(3)
# l2=linkedList()
l2=linkedList(5)
# l2.add(5)
# l2.add(6)
# l2.add(4)
print(sol.addTwoNumbers(l1,l2))