'''
*Question
Given Binary Search Tree, design an algorithm which creates a linkedlist of all nodes at each depth
'''

class llNode:
    def __init__(self,item):
        self.val = item
        self.next= None

class bstNode:
    def __init__(self,item):
        self.val = item
        self.left=None
        self.right=None

class LinkedList:
    # def __init__(self,item):
    #     self.head=llNode(item)
    #
    # def add(self,item):
    #     cur=self.head
    #     while cur.next is not None:
    #         cur=cur.next
    #     cur.next=llNode(item)

    def __init__(self):
        self.head=llNode(None)
        self.height=0
        # self.linkedlist=[]

    def add(self,item):
        if self.head.val is None:
            self.head.val=item
        else :
            cur=self.head
            while cur.next is not None:
                cur=cur.next
            cur.next = llNode(item)

    def length(self):
        cur = self.head
        length=0
        if cur.val is None:
            return 0
        else:
            while cur is not None:
                length=length+1
                cur=cur.next
            return length

    def printlinkedlist(self):
        linkedlist=[]
        cur =self.head
        while cur is not None:
            # print(cur.val)
            linkedlist.append(cur.val)
            cur=cur.next
        print(linkedlist)

class BinarySearchTree :
    def __init__(self):
        self.head = bstNode(None)
        self.linkedlists=[]
        self.inorder_list=[]

    def add(self,item):
        if self.head.val is None:
            self.head.val = item
        else :
            self.__add_node(self.head,item)

    def __add_node(self,cur,item):
        if cur.val <=item:
            if cur.right is not None:
                self.__add_node(cur.right,item)
            else :
                cur.right=bstNode(item)
        else:
            if cur.left is not None:
                self.__add_node(cur.left, item)
            else:
                cur.left=bstNode(item)

    def inorder_traverse(self):
        if self.head is not None:
            self.__inorder(self.head)

    def __inorder(self, cur):
        if cur.left is not None:
            self.__inorder(cur.left)
        self.inorder_list.append(cur.val)
        if cur.right is not None:
            self.__inorder(cur.right)

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

    def findLevelLinkedList(self):
        self.linkedlists = [LinkedList() for i in range(self.treeHeight())]
        ll=LinkedList()
        ll.add(self.head.val)
        self.linkedlists[0] = ll
        ll=LinkedList()
        return self.__findLevelLinkedList(self.head,1,ll)

    def __findLevelLinkedList(self,cur,level,ll):
        if cur is None :
            return False
        else :
            ll2=LinkedList()
            if cur.left is not None:
                ll.add(cur.left.val)
                print('cur.left.val ' ,cur.left.val)
                print('level ', level)
                self.__findLevelLinkedList(cur.left,level+1,ll2)
            if cur.right is not None:
                ll.add(cur.right.val)
                print('cur.right.val ', cur.right.val)
                print('level ', level)
                self.__findLevelLinkedList(cur.right,level+1,ll2)

            if ll.length() != 0 :
                print('**********ll.length()',ll.length())
                print('********level ', level)
                ll.printlinkedlist()
                self.linkedlists[level] = ll
                return self.linkedlists

            else :
                return False


bt = BinarySearchTree()
bt.add(5)
bt.add(3)
bt.add(7)
bt.add(2)
bt.add(4)
bt.add(6)
bt.add(9)
bt.add(10)
bt.add(11)
bt.add(12)
print('treeHeight ',bt.treeHeight())

linkedlists=bt.findLevelLinkedList()
print('len of linkedlists ',len(linkedlists))
for linkedlist in linkedlists:
    linkedlist.printlinkedlist()
#result not right -> due to misunderstanding of insert #####################다시 정리!!!!











