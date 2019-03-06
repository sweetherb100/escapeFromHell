'''
*Idea
Recursion
'''

class find_subsets_from_set:
    def sub_sets(self,set):
        subset = [None]*len(set) #to be updated as recursion
        return self.subsets_helper(set, subset, 0)

    #original set is needed to update the val of cur index
    def subsets_helper(self, set, subset, cur): #use 3 argument : original string, recursive subset, cur pos
        #base condition
        if cur == len(set): #reached the end
            print(subset)

        else : #recursion
            subset[cur] = None
            self.subsets_helper(set, subset, cur+1) #go for the next recursion
            subset[cur] = set[cur]
            self.subsets_helper(set, subset, cur + 1)  # go for the next recursion

print(find_subsets_from_set().sub_sets([1,2,3]))
