'''
Given a BST and a range, return the sum of all numbers contained in the BST that are also within that range. 
What is the runtime of your solution?  

Time complexity of the above program is O(h + k) where h is height of BST and k is number of nodes in given range.
'''

class Solution(object):
    def rangeSumBST(self, root, L, R):
        sum = 0
        stack = [root]

        while stack:
            node = stack.pop()
            if node:
                if L <= node.val <= R: #BE CAREFUL WITH EQUAL
                    ##CF) NOT RECURSIVE SO I CANNOT SAY THIS IS BASE CONDITION?!
                    sum += node.val

                if L < node.val: # DOESN"T HAVE EQUAL
                    stack.append(node.left)

                if node.val < R:
                    stack.append(node.right)

        return sum