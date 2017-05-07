'''
*Quesion
When there is sorted array, make binary tree with min height
=Make Binary Search Tree
'''

class Node :
    def __init__(self,item):
        self.val = item
        self.left = None
        self.right = None

class BinarySearchTree :
    def __init__(self):
        self.head = Node(None)
        self.inorder_list = []
        self.height=0

    def inorder_traverse(self):
        if self.head is not None:
            self.__inorder(self.head)

    def __inorder(self, cur):
        if cur.left is not None:
            self.__inorder(cur.left)
        self.inorder_list.append(cur.val)
        if cur.right is not None:
            self.__inorder(cur.right)

    def add(self,item):
        if self.head.val is None :
            self.head.val = item
        else :
            self.__add(self.head, item)

    def __add(self,cur,item):
        if cur.val <= item:
            if cur.right is not None:
                self.__add(cur.right,item)
            else :
                cur.right=Node(item)
        else:
            if cur.left is not None:
                self.__add(cur.left, item)
            else:
                cur.left=Node(item)

    #don't need to give cur(self.head) as parameter.
    def makeMinHeight(self,list):
        self.__makeMinHeight(list)
        bt.inorder_traverse()
        return bt.inorder_list

    def __makeMinHeight(self,list):
        if len(list) == 0:
            return False
        else :
            start=0
            end=len(list)-1
            mid = (start+end)//2
            print('list[mid] ',list[mid])
            # don't need to give cur(self.head) as parameter.
            #add method automatically add node in its right place by BST rule(whether it is left or right).
            self.add(list[mid])
            self.__makeMinHeight(list[:mid])
            self.__makeMinHeight(list[mid+1:])
            return True

    def treeHeight(self):
        if self.head.val is None:
            return 0
        else:
            return self.__tree_height(self.head,1)

    def __tree_height(self, cur, height):
        if cur.left is not None:
            self.height=height+1
            print('self.height in left ' ,self.height)
            print('cur.left.val',cur.left.val)
            self.__tree_height(cur.left, height+1)

        if cur.right is not None:
            self.height = height + 1
            print('self.height in right ', self.height)
            print('cur.right.val', cur.right.val)
            self.__tree_height(cur.right, height+1)

        if self.height > height:
            return self.height
        else :
            return height

bt= BinarySearchTree()
print(bt.makeMinHeight([1,3,5,6,7,8]))
print(bt.treeHeight())
# print('*********',bt.inorder_list)




