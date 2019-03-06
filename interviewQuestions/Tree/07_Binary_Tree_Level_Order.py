'''
Given a binary tree, return the level order traversal of its nodes’ values. (ie, from left to right, level by level).

Example :
Given binary tree

    3
   / \
  9  20
    /  \
   15   7
return its level order traversal as:

[
  [3],
  [9,20],
  [15,7]
]
'''


# Definition for a  binary tree node
class Node:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

### GRAPH : BREADTH FIRST SEARCH (QUEUE) WITH 2 WHILE LOOP!!!
class Solution:
    # @param A : root node of tree
    # @return a list of list of integers
    def levelOrder(self, A):
        result = []
        queue = []
        queue.append(A)  ####SHOULDNT USE A.val!!!
        result.append([A.val])

        while len(queue) > 0:
            temp = []
            tempNode = []

            while len(queue) > 0: #I have 9 and 20
                cur = queue.pop(0)
                if cur.left is not None:
                    temp.append(cur.left.val)  ### BE CAREFUL WITH VAL AND NODE
                    tempNode.append(cur.left)
                if cur.right is not None:
                    temp.append(cur.right.val)  ### BE CAREFUL WITH VAL AND NODE
                    tempNode.append(cur.right)

            ### IN THE LEAF NODE, THERE WOULD BE EMPTY TEMPNODE SO AFTER EXTENDING TO QUEUE, IT WILL BE EMPTY AND GO OUT OF WHILE LOOP
            result.append(temp)
            queue.extend(tempNode) ### THIS IS EXTEND!!!!

        result.pop()  #### BE CAREFUL!! pop the last one because it will be awlays []
        return result


  #        3
  #     /     \
  #    9       20
  #  /   \     /  \
  # 99   999  15   7

bt = Node(3)
bt.left=Node(9)
bt.left.left=Node(99)
bt.left.right=Node(999)

bt.right=Node(20)
bt.right.left=Node(15)
bt.right.right=Node(7)

sol = Solution()
print(sol.levelOrder(bt))



