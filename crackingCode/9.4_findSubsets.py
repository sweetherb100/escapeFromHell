'''
*Idea
Recursion

sub_sets([1,2])
=findSubset([],[1,2])
=findSubset([],[2]) + findSubset([1],[2])
=findSubset([],none) + findSubset([2],none) + findSubset([1],none) + findsubSet([1,2],none)
=[]+[2]+[1]+[1,2]
=[ [],[2],[1],[1,2] ]

sub_sets([1,2,3])
=findSubset([],[1,2,3])
=findSubset([],[2,3]) + findSubset([1],[2,3])
=findSubset([],[3])+findSubset([2],[3])+ findSubset([1],[3]) + findSubset([1,2],[3])
=findSubset([],none) + findSubset([3],none) + findSubset([2],none) + findSubset([2,3],none) +findSubset([1],none) + findSubset([1,3],none) +findsubSet([1,2],none) +findsubSet([1,2,3],none)
=[]+[3]+[2]+[2,3]+[1]+[1,3]+[1,2]+[1,2,3]
=[ [],[1],[2],[3],[1,2],[1,3],[2,3],[1,2,3] ]

*Python
1) When prev = [2,1], cur =3,
prev+[cur] -> [2,1] + [3] = [2,1,3]
'''

class find_subsets_from_set:
    def sub_sets(self,set):
        #start by adding an empty set to all possible subsets
        return self.findSubset([],set)

    def findSubset(self,prev,subset):
        if subset: #if subset is not None
            cur=subset[0]
            #findSubset(prev, next items) + findSubset(prev+current, next items)
            return self.findSubset(prev,subset[1:]) + self.findSubset(prev+[cur],subset[1:])
        return [prev]

print(find_subsets_from_set().sub_sets([2,1,3]))
