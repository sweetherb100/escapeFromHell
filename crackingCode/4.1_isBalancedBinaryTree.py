'''
*Question : Check whether a binary tree is balanced

*Tree : consists of Node. make Node class and BinaryTree class

*To think about 
Assumption is binary tree, not binary search tree.
is it okay to make tree in form of binary search tree?
'''

class Node:
    def __init__(self,item):
        self.val=item
        self.left=None
        self.right=None

class BinaryTree:
    def __init__(self):
        self.head=Node(None)

    def add(self,item):
        if self.head.val is None:
            self.head.val=item
        else:
            self.__add_node(self.head, item)

    def __add_node(self,cur,item):
        if item <= cur.val:
            if cur.left is not None:
                self.__add_node(cur.left,item)
            else:
                cur.left=Node(item)
        else:
            if cur.right is not None:
                self.__add_node(cur.right,item)
            else:
                cur.right=Node(item)

    def is_balanced(self):
        if self.checkHeight(self.head) == -1:
            return False
        else:
            return True

    def checkHeight(self,node):
        if node is None:
            return 0

        #if left subtree is balanced
        leftHeight=self.checkHeight(node.left)
        if leftHeight == -1:
            return -1

        #if right subtree is balanced
        rightHeight=self.checkHeight(node.right)
        if rightHeight == -1:
            return -1

        #if current node is balanced
        heightDiff= leftHeight-rightHeight
        if abs(heightDiff) > 1:
            return -1
        else :
            return max(leftHeight,rightHeight) +1

bt = BinaryTree()
bt.add(5)
bt.add(3)
# bt.add(1)
print(bt.is_balanced())