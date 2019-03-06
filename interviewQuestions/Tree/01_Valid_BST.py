'''
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

1) The left subtree of a node contains only nodes with keys "less than" the node’s key.
2) The right subtree of a node contains only nodes with keys "greater than" the node’s key.
3) Both the left and right subtrees must also be binary search trees.

'''
# Definition for a  binary tree node
class Node: #TreeNode
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # @param A : root node of tree
    # @return an integer
    def __init__(self):
        self.inorder=[]

    def in_order(self, A):
        if A.left is not None: ### DONT FORGET
            self.in_order(A.left)
        
        self.inorder.append(A.val)
        
        if A.right is not None:
            ls = self.in_order(A.right)
        
        
    def isValidBST(self, A):
        ### to valid BST, do inorder (LvR) traverse and see it is ascending order
        self.in_order(A)
        
        for i in range(len(self.inorder)-1):
            if self.inorder[i] >= self.inorder[i+1]: ### SHOULD ALSO CONTAIN EQUAL SIGN!!
                return 0  #not ascending order
                
        return 1

bt = Node(3)
bt.left=Node(2)
bt.right=Node(4)
bt.left.left=Node(1)
bt.left.right=Node(3)

# bt.add(3)
# bt.add(4)
# bt.add(1)
# bt.add(7)

solution = Solution()
print(solution.isValidBST(bt))
