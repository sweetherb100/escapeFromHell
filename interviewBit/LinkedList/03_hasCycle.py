'''
2 Approaches
1) Hash Map (save each element and see if there is duplicate) 
Time Complexity :O(n)
Space Complexity : O(n)

2) 2 pointers
Time Complexity : O(n)
Space Complexity : O(1)
'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        cur = head

        # Exception : empty linkedlist
        if cur is None:
            return False #no cycle

        # solve in Space Complexity O(1)
        slow = cur
        fast = cur.next

        while slow is not None and fast is not None: #SAME AS:  while slow and fast:
            if slow == fast:  # at some point, if they meet, there is cycle
                return True #cycle

            slow = slow.next
            if fast.next is not None: #SAME AS: fast.next
                fast = fast.next.next
            else:
                return False #no cycle

        return False #no cycle