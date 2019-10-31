'''
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
'''

#### COMPARE WITH CrackingCode : 4.3_binaryTreeWithMinHeight

# Definition for a  binary tree node
class Node: #TreeNode
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param A : root node of tree
    # @return an integer
    def minDepth(self, A):
        ### DO NOT START FROM A.left/ A.right
        # if A.left is None:
        #     return 1
        # if A.right is None:
        #     return 1

        if A is None:  # based condition
            return 0

        lheight = self.minDepth(A.left) + 1 #possible height when choose left-subtree
        rheight = self.minDepth(A.right) + 1 #possible height when choose right-subtree

        ## Exception : minDepth cannot be 1 (CASE : 1 2 -1 -1 -1)
        if lheight != 1 and rheight == 1:
            return lheight
        elif lheight == 1 and rheight != 1:
            return rheight


        if lheight < rheight:  # lheight has min height
            return lheight
        else:
            return rheight


#CASE1
# bt = Node(5)
# bt.left=Node(3)
# bt.right=Node(2)
# bt.left.left=Node(1)
# bt.left.left.right=Node(7)

#CASE2
bt = Node(1)
bt.left=Node(2)

sol=Solution()
print(sol.minDepth(bt))
