'''
Find the lowest common ancestor in an unordered binary tree given two values in the tree.
'''


# Definition for a  binary tree node
class Node:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param A : root node of tree
    # @param B : integer
    # @param C : integer
    # @return an integer
    def lca(self, tree, target1, target2):
        result = tree.val

        path1 = self.pathToTarget(tree, target1, [])
        path2 = self.pathToTarget(tree, target2, [])

        # path might be None (not len==0)
        if path1 is None or path2 is None:
            return -1

        while len(path1) != 0 and len(path2) != 0:
            val1 = path1.pop()
            val2 = path2.pop()
            if val1 == val2:
                result = val1
            else:
                break

        return result  # the latest pop which was the same

    def pathToTarget(self, tree, target, path):
        # base condition
        if tree is None:  # not found but just reached the leaf node
            return None

        # print(tree.val)

        if tree.val == target:  # starting from the end
            path.append(tree.val)  # first push
            return path

        leftPath = self.pathToTarget(tree.left, target, path)
        if leftPath is not Nne:
            path.append(tree.val)
            return path
        # else: If I do return None here, I will never have rightPath
        #     return None

        rightPath = self.pathToTarget(tree.right, target, path)
        if rightPath is not None:
            path.append(tree.val)
            return path
        # else:
        #     return None

        return None


bt = Node(3)
bt.left=Node(5)
bt.left.left=Node(6)
bt.left.right=Node(2)
bt.left.right.left=Node(7)
bt.left.right.right=Node(4)

bt.right=Node(1)
bt.right.left=Node(0)
bt.right.right=Node(8)

sol = Solution()
print(sol.lca(bt, 5,1))

