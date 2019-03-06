'''
Reverse a linked list from position m to n. 
Do it in-place and in one-pass.

For example:
Given 1->2->3->4->5->NULL, m = 2 and n = 4,

return 1->4->3->2->5->NULL.
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param A : head node of linked list
    # @param B : integer
    # @param C : integer
    # @return the head node in the linked list
    def reverseBetween(self, A, B, C):
        dummy=ListNode(0)
        cur=dummy
        cur1 = A

        # step 1: add to dummy until B-1th node
        for i in range(1,B): #starting from 1 (don't get confused with index)
            cur.next=cur1 #########cur.next will have the REST OF cur1 if linked like this BUT DOESNT MATTER BECAUSE BELOW, keep UPDATING LIKE cur.next=prev
            cur =cur.next #move forward
            cur1 = cur1.next #move forward

        # step 2 : make prev that is reversed linkedlist from B to Cth node
        prev=None
        for i in range(B, C+1):
            temp = cur1.next
            cur1.next=prev
            prev=cur1
            cur1=temp

        # step 3 : add reversed linkedlist to cur
        cur.next= prev

        # step 4 : move to the very end of cur
        while cur.next is not None:
            cur=cur.next

        # step 5: add the rest of node (after Cth node) to the cur
        cur.next=cur1

        return dummy.next

solution = Solution()
# l1 = ListNode(1)
# cur1=l1 #head
# cur1.next=ListNode(5)
# cur1 = cur1.next
# cur1.next=ListNode(7)
# cur1 = cur1.next
#
# cur1.next=ListNode(8)
# cur1 = cur1.next
# cur1.next=ListNode(2)
# cur1 = cur1.next
# cur1.next=ListNode(3)
# cur1 = cur1.next

# A : [ 83 -> 13 -> 21 -> 72 ]
# B : 1
# C : 4
# l1 = ListNode(83)
# cur1=l1 #head
# cur1.next=ListNode(13)
# cur1 = cur1.next
# cur1.next=ListNode(21)
# cur1 = cur1.next
# cur1.next=ListNode(72)
# cur1 = cur1.next

l1 = ListNode(1)
cur1=l1 #head
cur1.next=ListNode(2)
cur1 = cur1.next
cur1.next=ListNode(3)
cur1 = cur1.next

ll = solution.reverseBetween(l1, 2, 3)

while ll is not None:
    print(ll.val)
    ll=ll.next



### NEED TO IMPLEMENT DIFFERENTLY WHEN B=1 or B>=2
'''
cur = A

        for i in range(1,B-1):#until B-1
            cur = cur.next

        cur2 = cur #cur2=cur CORRECTED
        cur2=cur2.next
        print(cur.val)
        print(cur2.val)

        prev = None
        for i in range(B, C+1):
            next = cur2.next  # save the temp
            cur2.next = prev
            prev = cur2
            cur2 = next
            print(prev.val)

        cur.next = prev #I THINK cur = prev IS WRONG. SHOULD BE CONNECT WITH NEXT

        while cur.next is not None: # JUST TO SEND IT TO THE LAST, USE CUR.NEXT (SO THAT I CAN USE CUR.NEXT IN THE NEXT LINE)
            # print(cur.val)
            cur = cur.next

        # print(cur2.val)
        # print(cur.val)
        cur =cur2 #I THINK cur = cur2 IS WRONG. SHOULD BE CONNECT WITH NEXT

        print("************")
        return A
'''