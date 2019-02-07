'''
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.
Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
'''


class Node:
    def __init__(self,item):
        self.val =item
        self.next=None


class LinkedList:
    def __init__(self,item):
        self.head = Node(item)

    def add(self,item):
        cur=self.head
        while cur.next is not None:
            cur=cur.next
        cur.next=Node(item)

    def printlist(self):
        cur=self.head
        result=[]
        while cur is not None:
            result.append(cur.val)
            cur=cur.next
        return result

    def getHead(self):
        return self.head

    def mergeTwoLists(self, list1, list2):
        cur1=list1.head
        cur2=list2.head

        if cur1.val <= cur2.val:
            resultlist=LinkedList(cur1.val)
            cur1=cur1.next
        else:
            resultlist=LinkedList(cur2.val)
            cur2 = cur2.next

        while cur1 is not None and cur2 is not None: #AND
            if cur1.val <= cur2.val:
                resultlist.add(cur1.val)
                cur1=cur1.next
            else:
                resultlist.add(cur2.val)
                cur2 = cur2.next

        #good thing about add is that I don't have to send the linkedlist to the end but add function will do it for me!
        while cur1 is not None:
            resultlist.add(cur1.val)
            cur1=cur1.next

        while cur2 is not None:
            resultlist.add(cur2.val)
            cur2 = cur2.next

        return resultlist.printlist()






# 2 sorted list
list1 = LinkedList(1)
list1.add(2)
list1.add(4)

list2 = LinkedList(1)
list2.add(3)
list2.add(4)
print(list1.mergeTwoLists(list1, list2))
