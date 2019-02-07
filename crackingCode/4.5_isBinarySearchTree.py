'''
*Question : Implement an algorithm to find a given tree is Binary Search Tree
(This implementation will always be BST since it is added to form BST)

*Idea (BST criterion)
When inorder traverse (LvR) a tree and if it is ascending order, then it is BST

*Python
1) sorted(list) : return new_list of sorted list (for me, this is better)
2) list.sort() : no return. sort list
'''

class Node:
    def __init__(self,item):
        self.val=item
        self.left=None
        self.right=None

class BinarySearchTree:
    def __init__(self):
        self.head=Node(None)
        self.inorder_list=[]

    def add(self,item):
        if self.head.val is None:
            self.head.val=item
        else:
            self.__add(self.head, item)

    def __add(self,cur,item):
        if item <=cur.val:
            if cur.left is not None:
                self.__add(cur.left,item)
            else:
                cur.left=Node(item)
        else:
            if cur.right is not None:
                self.__add(cur.right,item)
            else:
                cur.right=Node(item)

    def inorder_traverse(self):
        if self.head is not None:
            self.__inorder(self.head)

    def __inorder(self,cur):
        if cur.left is not None:
            self.__inorder(cur.left)
        self.inorder_list.append(cur.val)
        if cur.right is not None:
            self.__inorder(cur.right)



bt = BinarySearchTree()
bt.add(5)
bt.add(3)
bt.add(4)
bt.add(1)
bt.add(7)
bt.inorder_traverse()

#if inorder_list is sorted, then it is BST
orig = bt.inorder_list
comp = sorted(orig)
print(orig) #[1, 3, 4, 5, 7]
print(comp) #[1, 3, 4, 5, 7]

if orig == comp:
    print('this is bst')
else :
    print('this is not bst')


