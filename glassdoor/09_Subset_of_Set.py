'''
*Recursion
'''

### RETURN THE LIST OF LIST
class find_subsets_from_set:
    def __init__(self):
        self.ls=[]

    def sub_sets(self, set):
        subset = [None] * len(set)  # to be updated as recursion, set the length and value in advance (just need to overwrite on top)
        self.subsets_helper(set, subset, 0)
        return self.ls

    # original set is needed to update the val of cur index
    def subsets_helper(self, set, subset, cur):  # use 3 argument : original list, recursive subset, cur pos
        # base condition : reached the end
        if cur == len(set):
            self.ls.append(subset[::]) #copy by value the list
            return

        # 2 recursion
        subset[cur] = None
        self.subsets_helper(set, subset, cur + 1)  # go for the next index
        subset[cur] = set[cur]
        self.subsets_helper(set, subset, cur + 1)  # go for the next index

print(find_subsets_from_set().sub_sets([1, 2, 3]))
