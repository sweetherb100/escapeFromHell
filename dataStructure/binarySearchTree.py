'''
* Binary Search Tree(MUST KNOW!!)
1) good performance
2) Recursion
3) Search, Delete, Insert : O(log n)
cf) LinkedList의 Search, Delete, Insert : O(n) (very slow)
4) Tree : consists of Node. 

*Definition
1) left subtree node is smaller than or equal to parent node.
1) right subtree node is bigger than or equal to parent node.

*Binary Search Tree criterion
:when inorder traverse (LvR) a tree and if it is ascending order, then it is BST
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

    def search(self, item):
        if self.head.val is None:
            return False
        else:
            return self.__search_node(self.head, item)

    def __search_node(self, cur, item):
        if cur.val == item:
            return True
        else:
            if cur.val >= item:
                if cur.left is not None:
                    return self.__search_node(cur.left, item)
                else:
                    return False
            else:
                if cur.right is not None:
                    return self.__search_node(cur.right, item)
                else:
                    return False

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

# Remove 1 : Node to be removed has no child -> Just remove it
# Remove 2 : Node to be removed has one child -> Kill parent, and link with grandparent
# Remove 3 : Node to be removed has two children
# -> change with the very left node of left subtree

    def remove(self,item):
        if self.head.val is None:
            print("there is no item:in BST",item)
        if self.head.val==item:
            # 1) Node to be removed has no children
            if self.head.left is None and self.head.right is None:
                self.head=None
            # 2) Node to be removed has one child
            elif self.head.left is None and self.head.right is not None:
                self.head=self.head.right
            # 2) Node to be removed has one child
            elif self.head.left is not None and self.head.right is None:
                self.head=self.head.left
            # 3) Node to be removed has two children
            else:
                self.head.val=self.__most_left_val_from_right_node(self.head.right).val
                self.__removeitem(self.head, self.head.right, self.head.val)
                #Remove node of self.head's right subtree
        else:
            if self.head.val > item:
                self.__remove(self.head, self.head.left, item)
            else :
                self.__remove(self.head, self.head.right, item)

    def __remove(self, parent, cur, item):
        if cur is None:
            print ("There is no item: ", item)
        if cur.val == item:
            # 1) Node to be removed has no children.
            if cur.left is None and cur.right is None:
                if parent.left == cur:
                    parent.left = None
                else:
                    parent.right = None
            # 2) Node to be removed has one child.
            elif cur.left is None and cur.right is not None:
                if parent.left == cur:
                    parent.left = cur.right
                else:
                    parent.right = cur.right
            # 2) Node to be removed has one child.
            elif cur.left is not None and cur.right is None:
                if parent.left == cur:
                    parent.left = cur.left
                else:
                    parent.right = cur.left
            # 3) Node to be removed has two children.
            else:
                cur.val = self.__most_left_val_from_right_node(cur.right).val
                self.__removeitem(cur, cur.right, cur.val)
        else:
            if self.head.val > item:
                self.__remove(cur, cur.left, item)
            else:
                self.__remove(cur, cur.right, item)

    def __most_left_val_from_right_node(self,cur): #cur : eventually, right subtree node will come
        if cur.left is None:
            return cur
        else:
            return self.__most_left_val_from_right_node(cur.left)

    def __removeitem(self,parent,cur,item):
        if cur.val==item:
            if parent.left==cur:
                parent.left=None
            else:
                parent.right=None
        else:
            if cur.val>item:
                self.__removeitem(cur,cur.left,item)
            else :
                self.__removeitem(cur,cur.right,item)

    def preorder_traverse(self):
        if self.head is not None:
            self.__preorder(self.head)

    def __preorder(self, cur):
        self.preorder_list.append(cur.val)
        print (cur.val)
        if cur.left is not None:
            self.__preorder(cur.left)
        if cur.right is not None:
            self.__preorder(cur.right)

bt = BinarySearchTree()
# bt.add(5)
# bt.add(3)
# bt.add(4)
# bt.add(1)
# bt.add(7)
# #      5
# #    3     7
# # 1     4

bt.add(1)
bt.add(2)
bt.add(3)
bt.add(4)
bt.preorder_traverse()
print("pre order")
bt.remove(1)
bt.preorder_traverse()
print("pre order")

print(bt.search(3))
print(bt.search(999))








