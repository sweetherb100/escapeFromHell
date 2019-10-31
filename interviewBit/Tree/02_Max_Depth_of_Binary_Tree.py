'''
Given a binary tree, find its maximum depth.
The maximum depth of a binary tree is the number of nodes along the longest path from the root node down to the farthest leaf node.

'''

### COMPARE WITH crackingCode : 4.1_isBalancedBinaryTree
class Node:
    def __init__(self,item):
        self.val=item
        self.left=None
        self.right=None

class Solution():
    def maxDepth(self, A):
        if A is None:
            return 0  # go down until the node is None (i.e. base condition)

        return 1 + max(self.maxDepth(A.left), self.maxDepth(A.right))


bt = Node(5)
bt.left=Node(3)
bt.right=Node(2)
bt.left.left=Node(1)
bt.left.left.right=Node(7)

sol=Solution()
print(sol.maxDepth(bt))
'''
# crackingCode : 4.1_isBalancedBinaryTree
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
        if leftHeight == -1:
            return -1

        rightHeight=self.checkHeight(node.right)
        # if the left subtree is not balanced, then the whole tree is not balanced
        if rightHeight == -1:
            return -1

        #if the difference in heights is greater than 1, the whole tree is not balanced
        heightDiff= leftHeight-rightHeight
        if abs(heightDiff) > 1:
            return -1
        else :
            return max(leftHeight,rightHeight) +1

'''