#Measure the path between two routes.
# 1) construct BST (consists of Nodes)
class Node:
    def __init__(self, item):
        self.val = item
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.head = Node(None)
        self.inorder_list = []

    def add(self, item):
        if self.head.val is None:
            self.head.val = item
        else:
            self.__add_node(self.head, item)

    def __add_node(self, cur, item):
        if cur.val >= item:
            if cur.left is not None:
                self.__add_node(cur.left, item)
            else:
                cur.left = Node(item)
        else:
            if cur.right is not None:
                self.__add_node(cur.right, item)
            else:
                cur.right = Node(item)

    def inorder_traverse(self):
        if self.head is not None:
            self.__inorder(self.head)

    def __inorder(self, cur):
        if cur.left is not None:
            self.__inorder(cur.left)
        self.inorder_list.append(cur.val)
        if cur.right is not None:
            self.__inorder(cur.right)

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

    def measurePath(self, start, end):
        if self.search(start) is False or self.search(end) is False:
            return False
        else :
            return self.__measurePath(self.head,start,end)

    def __measurePath(self,cur,start,end):
        if start < cur.val and end < cur.val : #same left subtree
            #start <= cur.val and end <= cur.val (X) -> When either of it is root, it undergoes noe more recursion. wrong!
            return self.__measurePath(cur.left,start,end)
        elif cur.val < start and cur.val < end : #same right subtree
            return self.__measurePath(cur.right,start,end)
        else :
            return (self.__measureDepth(cur,start,0) +self.__measureDepth(cur,end,0))

    def __measureDepth(self, cur, item, depth):
        if cur.val == item:
            print('depth ',depth)
            return depth
        else:
            if item <= cur.val:
                if cur.left is not None:
                    depth = depth+1
                    return self.__measureDepth(cur.left,item,depth)

            else:
                if cur.right is not None:
                    depth = depth + 1
                    return self.__measureDepth(cur.right, item,depth)

def bstDistance(values, n, node1, node2):
    # create bst using values
    bt = BinarySearchTree()
    for value in values:
        bt.add(value)
    bt.inorder_traverse()
    # okay. I made bst. 2) then how to calculate the path?
    return bt.measurePath(node1, node2)


print(bstDistance([5,6,3,1,2,4],6,5,1))
# print(bstDistance([9, 7, 5, 3, 1], 5, 7, 20))