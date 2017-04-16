# Binary Search Tree(인터뷰때 반드시 알고있어야 됨)
# 퍼포먼스 상당히 좋음
# Recursion 개념도 확인 가능
# Search, Delete, Insert : O(log n)
# cf) LinkedList의 Search, Delete, Insert : O(n)으로 상당히 느림
# 특징
# 1) 왼쪽 부트리 노드는 부모 노드보다 작거나 같다.
# 2) 오른쪽 부트리 노드는 부모 노드보다 크거나 같다.
#
# 트리 : 노드들의 구성체. 노드들이 서로 연결된 것

class Node:
    def __init__(self,item):
        self.val = item
        self.left = None
        self.right = None

class BinarySearchTree:

    def __init__(self):
        self.head=Node(None)
        self.preorder_list = []

    def search(self, item):  # 2가지 경우 1) Tree가 None인 경우 2) 아닌 경우
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
                    return self.__search_node(cur.left, item)  # 재귀함수로 leaf node로 내려가기
                else:
                    return False
            else:
                if cur.right is not None:
                    return self.__search_node(cur.right, item)  # 재귀함수로 leaf node로 내려가기
                else:
                    return False

    def add(self,item): #2가지 경우 1) Tree가 None인 경우 2) 아닌 경우
        if self.head.val is None:
            self.head.val = item
        else :
            self.__add_node(self.head,item)

    def __add_node(self, cur,item):
        if cur.val >= item:
            if cur.left is not None:
                self.__add_node(cur.left,item) #재귀함수로 leaf node로 내려가기
            else:
                cur.left=Node(item)
        else :
            if cur.right is not None:
                self.__add_node(cur.right,item) #재귀함수로 leaf node로 내려가기
            else :
                cur.right = Node(item)

# Remove 1 : Node to be removed has no child -> 그냥 없애면 됨
# Remove 2 : Node to be removed has one child -> 부모를 죽이고, 할아버지와 연결
# Remove 3 : Node to be removed has two children
# -> 오른쪽에 있는 서브트리의 가장 왼쪽 노드와 자리 바꿔주기

    def remove(self,item):
        if self.head.val is None:
            print("there is no item:in BST",item)
        if self.head.val==item:
            # 1) Node to be removed has no children
            if self.head.left is None and self.head.right is None:
                self.head=None
            # 2) Node to be removed has one child
            elif self.head.left is None and self.head.right is not None:
                # self.head.val = self.head.right.val
                # self.head.right=None
                self.head=self.head.right
                #########################질문올리기
            # 2) Node to be removed has one child
            elif self.head.left is not None and self.head.right is None:
                # self.head.val=self.head.left.val
                # self.head.left=None
                self.head=self.head.left
                #########################질문올리기
            # 3) Node to be removed has two children
            else:
                self.head.val=self.__most_left_val_from_right_node(self.head.right).val
                self.__removeitem(self.head, self.head.right, self.head.val)
                #self.head 기준으로 right 부트리 방향으로 노드를 지워라
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

    def __most_left_val_from_right_node(self,cur): #cur : 오른쪽 부트리 node값이 넘어온다.
        if cur.left is None:
            return cur
        else:
            return self.__most_left_val_from_right_node(cur.left) #재귀함수

    def __removeitem(self,parent,cur,item):
        if cur.val==item: #parent의 바로 자식 노드가 item 일 경우
            if parent.left==cur:
                parent.left=None
            else:
                parent.right=None
        else:
            if cur.val>item:
                self.__removeitem(cur,cur.left,item) #재귀함수
            else :
                self.__removeitem(cur,cur.right,item) #재귀함수

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








