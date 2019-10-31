'''
You are given two linked lists representing two non-negative numbers. 
The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8

    342 + 465 = 807
Make sure there are no trailing zeros in the output list
So, 7 -> 0 -> 8 -> 0 is not a valid response even though the value is still 807.
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


### THE LENGTH CAN BE DIFFERENT
### LETS MAKE THIRD LINK LIST (TRICK: INITIALZE WITH 0 NODE AND RETURN cur.next)
class Solution:
    # @param A : head node of linked list
    # @param B : head node of linked list
    # @return the head node in the linked list

    def addTwoNumbers(self, A, B):
        cur1 = A
        cur2 = B

        dummy = ListNode(0)
        cur=dummy
        carry = 0

        while cur1 is not None and cur2 is not None:
            temp = cur1.val + cur2.val + carry
            cur.next = ListNode(temp % 10)
            carry = temp // 10
            cur1 = cur1.next
            cur2 = cur2.next
            cur = cur.next

        # cur1 is longer
        while cur1 is not None:
            temp = cur1.val + carry
            cur.next = ListNode(temp % 10)
            carry = temp // 10
            cur1 = cur1.next
            cur = cur.next

        # cur2 is longer
        while cur2 is not None:
            temp = cur2.val + carry
            cur.next = ListNode(temp % 10)
            carry = temp // 10
            cur2 = cur2.next
            cur = cur.next

        if carry == 1:
            cur.next = ListNode(carry)

        return dummy.next


solution = Solution()
# (2 -> 4 -> 3) + (5 -> 6 -> 4)
# l1 = ListNode(2)
# cur1=l1 #head
# cur1.next=ListNode(4)
# cur1 = cur1.next # I SHOULD WRITE THIS OR ELSE I KEEP OVERWRITING ON TOP
# cur1.next=ListNode(3)
# cur1 = cur1.next
#
# l2 = ListNode(5)
# cur2=l2 #head
# cur2.next=ListNode(6)
# cur2 = cur2.next
# cur2.next=ListNode(4)
# cur2 = cur2.next

l1 = ListNode(0)

l2 = ListNode(1)
cur2=l2 #head
cur2.next=ListNode(0)
cur2 = cur2.next
cur2.next=ListNode(1)
cur2 = cur2.next

ll = solution.addTwoNumbers(l1, l2)
while ll is not None:
    print(ll.val)
    ll=ll.next