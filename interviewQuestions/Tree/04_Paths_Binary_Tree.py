'''
Given a binary tree, return all root-to-leaf paths.

Note: A leaf is a node with no children.

Example:
Input:

   1
 /   \
2     3
 \
  5

Output: ["1->2->5", "1->3"]
Explanation: All root-to-leaf paths are: 1->2->5, 1->3
'''

# Definition for a  binary tree node
class Node: #TreeNode
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def binaryTreePaths(self, root):
        if not root:
            return []

        res = []
        stack = [(root, "")] #save as tuple : (root, "")

        while stack:
            node, ls = stack.pop()

            if not node.left and not node.right: #if it is the leaf, just add the number
                res.append(ls+str(node.val)) #append the whole ls because it is the leaf (number of leaf represents number of path)

            if node.right:
                stack.append((node.right, ls + str(node.val) + "->"))

            if node.left: #node.left is second if clause
                stack.append((node.left, ls + str(node.val) + "->"))

        return res

bt = BinarySearchTree(1)
bt.left=Node(2)
bt.left.left=Node(10)
bt.left.right=Node(5)
bt.left.right.left=Node(8)
bt.right=Node(3)
# in this case,there exists 3paths

solution = Solution()
print(solution.binaryTreePaths(bt))
