from operator import mul
"""
1.1
WWPD

"one"

oneone

"two"

boo!

"aabb"
"""

#2.1
def sum_nums(lnk):
    """
    >>> a = Link(1, Link(6, Link(7)))
    >>> sum_nums(a)
    14
    """
    if lnk.rest is Link.empty:
        return lnk.first
    else:
        return lnk.first + sum_nums(lnk.rest)

#2.2
def multiply_lnks(lst_of_lnks):
    """
    >>> a = Link(2, Link(3, Link(5)))
    >>> b = Link(6, Link(4, Link(2)))
    >>> c = Link(4, Link(1, Link(0, Link(2))))
    >>> p = multiply_lnks([a, b, c])
    >>> p.first
    48
    >>> p.rest.first
    12
    >>> p.rest.rest.rest is Link.empty
    True
    """
    new_label = 1
    for lst in lst_of_lnks:
        new_label *= lst.first
    remaining_lst = [lst.rest for lst in lst_of_lnks]
    if Link.empty not in remaining_lst:
        return Link(new_label, multiply_lnks(remaining_lst))
    else:
        return Link(new_label)

#2.3
def flip_two(lnk):
    """
    >>> one_lnk = Link(1)
    >>> flip_two(one_lnk)
    >>> one_lnk
    Link(1)
    >>> lnk = Link(1, Link(2, Link(3, Link(4, Link(5)))))
    >>> flip_two(lnk)
    >>> lnk
    Link(2, Link(1, Link(4, Link(3, Link(5)))))
    """
    if lnk is not Link.empty and lnk.rest is not Link.empty:
        temp = lnk.first
        lnk.first = lnk.rest.first
        lnk.rest.first = temp
        flip_two(lnk.rest.rest)

#2.4
def filter_link(link, f):
    """
    >>> link = Link(1, Link(2, Link(3)))
    >>> g = filter_link(link, lambda x: x % 2 == 0)
    >>> next(g)
    2
    >>> next(g)
    StopIteration
    >>> list(filter_link(link, lambda x: x % 2 != 0))
    [1, 3]
    """
    while link is not Link.empty:
        if f(link.first) == True:
            yield link.first
        link = link.rest

#3.1
def make_even(t):
    """
    >>> t = Tree(1, [Tree(2, [Tree(3)]), Tree(4), Tree(5)])
    >>> make_even(t)
    >>> t.label
    2
    >>> t.branches[0].branches[0].label
    4
    """
    if t.label % 2 != 0:
        t.label += 1
    if not t.is_leaf():
        for branch in t.branches:
            make_even(branch)

#3.2
def square_tree(t):
    """Mutates a Tree t by squaring all its elements."""
    t.label *= t.label
    if not t.is_leaf():
        for branch in t.branches:
            square_tree(branch)

#3.3
def find_paths(t, entry):
    """
    >>> tree_ex = Tree(2, [Tree(7, [Tree(3), Tree(6, [Tree(5), Tree(11)])]), Tree(1, [Tree(5)])])
    >>> find_paths(tree_ex, 5)
    [[2, 7, 6, 5], [2, 1, 5]]
    >>> find_paths(tree_ex, 12)
    []
    """
    paths = []
    if t.label == entry:
        paths.append([t.label])
        return paths
    for branch in t.branches:
        for path in find_paths(branch,entry):
            paths.append(path)
    return [[t.label]+path for path in paths]

#3.4
def combine_tree(t1, t2, combiner):
    """
    >>> a = Tree(1, [Tree(2, [Tree(3)])])
    >>> b = Tree(4, [Tree(5, [Tree(6)])])
    >>> combined = combine_tree(a, b, mul)
    >>> combined.label
    4
    >>> combined.branches[0].label
    10
    """
    if t1.is_leaf() and t2.is_leaf():
        return Tree(combiner(t1.label, t2.label))
    else:
        new_branches = []
        combined_branches = zip(t1.branches,t2.branches)
        for c_b in combined_branches:
            new_branches.append(combine_tree(c_b[0], c_b[1], combiner))
        return Tree(combiner(t1.label, t2.label),new_branches)

#3.5
def alt_tree_map(t, map_fn):
    """
    >>> t = Tree(1, [Tree(2, [Tree(3)]), Tree(4)])
    >>> negate = lambda x: -x
    >>> alt_tree_map(t, negate)
    Tree(-1, [Tree(2, [Tree(-3)]), Tree(4)])
    """
    def helper(t, depth):
        if depth % 2 == 0:
            t.label = map_fn(t.label)
        if not t.is_leaf():
            for branch in t.branches:
                #calling helper on remaining branch with depth + 1 allows the same process to carry on going "down" the tree
                helper(branch,depth+1)
    helper(t,0)

    


#Linked list implementation#

class Link:
    empty = ()
    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.rest:
            rest_str = ', ' + repr(self.rest)
        else:
            rest_str = ''
            return 'Link({0}{1})'.format(repr(self.first), rest_str)
        
    def __str__(self):
        string = '<'
        while self.rest is not Link.empty:
            string += str(self.first) + ' '
            self = self.rest
        return string + str(self.first) + '>'

#tree implementation#
class Tree:
    def __init__(self, label, branches=[]):
        for b in branches:
            assert isinstance(b, Tree)
        self.label = label
        self.branches = branches
    
    def is_leaf(self):
        return not self.branches
    
    def print_tree(self,indent = 0):
        print('  ' * indent + str(self.label))
        for b in self.branches:
            b.print_tree(indent + 1)


