'''
*Question : Check whether a binary tree is balanced

*To think about 
Assumption is binary tree, not binary search tree.
is it okay to make tree in form of binary search tree?

"balanced" : the difference in height is 0 or 1
'''

class Node:
    def __init__(self,item):
        self.val=item
        self.left=None
        self.right=None


class Solution():
    def is_balanced(self, root):
        if self.checkHeight(root) == -1:
            return False
        else:
            return True

    def checkHeight(self,node):
        # None tree is balanced
        if node is None:
            return 0

        leftHeight=self.checkHeight(node.left)
        #if the left subtree is not balanced, then the whole tree is not balanced
        if leftHeight == -1: #if returned -1 in the previous recursion, just return -1 again
            return -1

        rightHeight=self.checkHeight(node.right)
        # if the left subtree is not balanced, then the whole tree is not balanced
        if rightHeight == -1: #if returned -1 in the previous recursion, just return -1 again
            return -1

        #if the difference in heights is greater than 1, the whole tree is not balanced
        heightDiff= leftHeight-rightHeight
        if abs(heightDiff) > 1:
            return -1
        else :
            return max(leftHeight,rightHeight) +1

bt = Node(5)
bt.left=Node(3)
bt.right=Node(2)
bt.left.left=Node(1)
bt.left.left.right=Node(7)

sol = Solution()
print(sol.is_balanced(bt))