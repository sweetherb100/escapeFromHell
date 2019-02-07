'''
*Question :
You have two very large binary search trees:
T1, with millions of nodes, and T2, with hundreds of nodes.
Create an algorithm to decide if T2 is a subtree of T1

*Idea :
1) search the root of T2 in T1
2) if you found root of T2 in T1, traverse T1 from that node and also traverse T2
3) if it is a match, T2 is a subtree of T1

*Python
1) ex) [6, 7, 9], [6, 7, 8, 9] subset + order match
ex) 
i = 0
j = 0
while (i < len(inorderList1)):
    if inorderList1[i] == inorderList2[j]:
        i = i + 1
    elif (inorderList1[i] != inorderList2[j]) and i != 0:
        return False
        break
    j = j + 1
return True

2) set(list) : [ ] -> { } transform
3) issubset : subset relationship
ex) 
if set(inorderList1).issubset(set(inorderList2)) :
    return True
else :
    return False

'''

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


    def getHead(self):
        return self.head

    # changed name (original : search__index)
    def update__index(self,item):
        if self.head.val is None:
            return False
        else:
            self.__update_indexnode(self.head,item)

    # changed name (original : __search_indexnode)
    def __update_indexnode(self,cur,item):
        if cur.val == item:
            self.head= cur
        else:
            if item <=cur.val:
                if cur.left is not None:
                    self.__update_indexnode(cur.left,item)

            else:
                if cur.right is not None:
                    self.__update_indexnode(cur.right,item)

def Solution(T2, T1):
    bst2=BinarySearchTree()
    bst1=BinarySearchTree()
    for node in T2:
        bst2.add(node)
    for node in T1:
        bst1.add(node)


    if bst2.search(bst1.getHead().val) is False :
        return False
    else : #for sure, bst1 root exists in bst2 tree; #traverse and compare
        bst1.inorder_traverse()
        inorderList1=bst1.inorder_list
        print(inorderList1) #[7, 8, 9]

        bst2.update__index(bst1.head.val) #updated the head of bst2
        bst2.inorder_traverse() #[7, 8, 9]
        inorderList2 = bst2.inorder_list
        print(inorderList2)

        # for sure, bst1 root exists in bst2 tree
        for i in range(len(inorderList1)):
            if inorderList2[i] != inorderList1[i]:
                return False
        return True


print(Solution([1,2,3,5,6,7,8,9],[7,8,9]))







    