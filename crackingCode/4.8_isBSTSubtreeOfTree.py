class Node:
    def __init__(self,item):
        self.val = item
        self.left=None
        self.right=None

class BinarySearchTree:
    def __init__(self):
        self.head=Node(None)
        self.inorder_list=[]

    def add(self,item):
        if self.head.val is None:
            self.head.val = item
        else :
            self.__add_node(self.head,item)

    def __add_node(self,cur,item):
        if item <= cur.val:
            if cur.left is not None:
                self.__add_node(cur.left,item)
            else :
                cur.left=Node(item)
        else:
            if cur.right is not None:
                self.__add_node(cur.right,item)
            else:
                cur.right=Node(item)

    def search(self,item):
        if self.head.val is None:
            return False
        else:
            return self.__search_node(self.head,item)

    def __search_node(self,cur,item):
        if cur.val == item:
            return True
        else:
            if item <=cur.val:
                if cur.left is not None:
                    self.__search_node(cur.left,item)
                else:
                    return False
            else:
                if cur.right is not None:
                    self.__search_node(cur.right,item)
                else:
                    return False

    def inorder_traverse(self):
        if self.head is not None:
            self.__inorder(self.head)

    def __inorder(self,cur):
        if cur.left is not None:
            self.__inorder(cur.left)

        self.inorder_list.append(cur.val)

        if cur.right is not None:
            self.__inorder(cur.right)

    def printInorderList(self):
        return self.inorder_list

    