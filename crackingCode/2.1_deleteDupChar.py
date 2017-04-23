'''
Time Complexity : O(n)
Space Complexity : O(n)

*remove duplicate Outline :
1) use Dictionary (Hash)
2) use prev Node (to link with previous and next node)

*Python
1) Dictionary (order doesn't always match)
dict = {
    'one':1,
    'two':2
}
dict['one']=11 #change
dict['three']=3 #add
del(dict['one'])
print(dict.pop('two')) #remove. return the first index

for key in ages.keys():
    print(key)
for value in ages.values():
    print(value)
for key in ages:
    print('{} age : {}.'.format(key, ages[key]))
for key, value in ages.items():
    print('{} age :{}.'.format(key, value))
'''


class Node:
    def __init__(self,item):
        self.val=item
        self.next=None

class LinkedList:
    def __init__(self,item):
        self.head = Node(item)

    def add(self,item):
        cur=self.head
        while cur.next is not None:
            cur=cur.next
        cur.next = Node(item)

    def printlist(self):
        cur=self.head
        res=[]
        while cur is not None:
            res.append(cur.val)
            cur=cur.next
        return res

    def delete_duplicate (self):
        cur = self.head
        dict ={}
        prev =None

        while cur is not None:
            if cur.val in dict:
                prev.next=cur.next
            else :
                dict[cur.val]=True
                prev = cur
            cur = cur.next

ll=LinkedList(3)
ll.add(4)
ll.add(5)
ll.add(6)
ll.add(4)
ll.add(7)
ll.add(4)
ll.add(6)
ll.add(6)
ll.delete_duplicate()
print(ll.printlist())
