'''
1) preorder traverse (vLR)
When use preorder?
: When there are multiple servers,
send tree structure of one certain server to another server in preorder.

2) inorder traverse(LvR)
Time complexity : O(n)

3) postorder traverse(LRv)
'''

class Node:
    def __init__(self,item):
        self.val = item
        self.left = None
        self.right = None

class BinarySearchTree:

    def __init__(self):
        self.head=Node(None)
        self.preorder_list = []
        self.inorder_list = []
        self.postorder_list = []

    def add(self,item):
        if self.head.val is None:
            self.head.val = item
        else :
            self.__add_node(self.head,item)

    def __add_node(self, cur,item):
        if cur.val >= item:
            if cur.left is not None:
                self.__add_node(cur.left,item)
            else:
                cur.left=Node(item)
        else :
            if cur.right is not None:
                self.__add_node(cur.right,item)
            else :
                cur.right = Node(item)

    def preorder_traverse(self):
        if self.head is not None:
            self.__preorder(self.head)

    def __preorder(self,cur):
        self.preorder_list.append(cur.val)
        print(cur.val)
        if cur.left is not None:
            self.__preorder(cur.left)
        if cur.right is not None:
            self.__preorder(cur.right)

    def inorder_traverse(self):
        if self.head is not None:
            self.__inorder(self.head)

    def __inorder(self,cur):
        if cur.left is not None:
            self.__inorder(cur.left)
        self.inorder_list.append(cur.val)
        print(cur.val)
        if cur.right is not None:
            self.__inorder(cur.right)

    def postorder_traverse(self):
        if self.head is not None:
            self.__postorder(self.head)

    def __postorder(self,cur):
        if cur.left is not None:
            self.__postorder(cur.left)
        if cur.right is not None:
            self.__postorder(cur.right)
        self.postorder_list.append(cur.val)
        print(cur.val)


bt = BinarySearchTree()
bt.add(5)
bt.add(3)
bt.add(4)
bt.add(1)
bt.add(7)
#      5
#    3     7
# 1     4

bt.preorder_traverse() #vLR
# 5 3 1 4 7
print("pre order")
bt.inorder_traverse() #LvR
# 1 3 4 5 7
print("in order")
bt.postorder_traverse() #LRv
# 1 4 3 7 5
print("post order")








