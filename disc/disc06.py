def height(t):
    if is_leaf(t):
        return 0
    else:
        return 1 + max([height(branch) for branch in branches(t)])
    
def max_path_sum(t):
    """Return the maximum path sum of the tree.
    >>> t = tree(1, [tree(5, [tree(1), tree(3)]), tree(10)])
    >>> max_path_sum(t)
    11
    """
    if is_leaf(t):
        return label(t)
    else:
        return label(t) + max([max_path_sum(branch) for branch in branches(t)])

def square_tree(t):
    if is_leaf(t):
        return tree(label(t)*label(t))
    else:
        return tree(label(t)*label(t),[square_tree(branch) for branch in branches(t)])

    
def find_path(tree, x):
    """
    >>> t = tree(2, [tree(7, [tree(3), tree(6, [tree(5), tree(11)])] ), tree(15)])
    >>> find_path(t, 5)
    [2, 7, 6, 5]
    >>> find_path(t, 10) # returns None
    """
    if label(tree) == x:
        return [x]
    for branch in branches(tree):
        path = find_path(branch,x)
        if path != None:
            return [label(tree)] + path

def prune_binary(t,nums):
    if is_leaf(t):
        if label(t) in nums:
            return t
        return None
    else:
        next_valid_nums = [num[1:] for num in nums if num[0] == label(t)]
        new_branches = []
        #keep nums that begins with binary num == label(t)
        for branch in branches(t):
            pruned_branch = prune_binary(branch,next_valid_nums)
            if pruned_branch != None:
                new_branches = new_branches + pruned_branch
        if new_branches == []:
            return None
        return tree(label(t),new_branches)










#tree adt implementation
def tree(label, branches=[]):
    """Construct a tree with the given label value and a list of branches."""
    if change_abstraction.changed:
        for branch in branches:
            assert is_tree(branch), 'branches must be trees'
        return {'label': label, 'branches': list(branches)}
    else:
        for branch in branches:
            assert is_tree(branch), 'branches must be trees'
        return [label] + list(branches)

def label(tree):
    """Return the label value of a tree."""
    if change_abstraction.changed:
        return tree['label']
    else:
        return tree[0]

def branches(tree):
    """Return the list of branches of the given tree."""
    if change_abstraction.changed:
        return tree['branches']
    else:
        return tree[1:]

def is_tree(tree):
    """Returns True if the given tree is a tree, and False otherwise."""
    if change_abstraction.changed:
        if type(tree) != dict or len(tree) != 2:
            return False
        for branch in branches(tree):
            if not is_tree(branch):
                return False
        return True
    else:
        if type(tree) != list or len(tree) < 1:
            return False
        for branch in branches(tree):
            if not is_tree(branch):
                return False
        return True

def is_leaf(tree):
    """Returns True if the given tree's list of branches is empty, and False
    otherwise.
    """
    return not branches(tree)

def print_tree(t, indent=0):
    """Print a representation of this tree in which each node is
    indented by two spaces times its depth from the root.

    >>> print_tree(tree(1))
    1
    >>> print_tree(tree(1, [tree(2)]))
    1
      2
    >>> numbers = tree(1, [tree(2), tree(3, [tree(4), tree(5)]), tree(6, [tree(7)])])
    >>> print_tree(numbers)
    1
      2
      3
        4
        5
      6
        7
    """
    print('  ' * indent + str(label(t)))
    for b in branches(t):
        print_tree(b, indent + 1)

def change_abstraction(change):
    change_abstraction.changed = change

change_abstraction.changed = False

#compute maximum profit from a tree and cannot use nodes connected together by edges
def profit(t):
    """Return the max profit from a tree.
    >>> t = tree(5,[tree(3),tree(4,[tree(5)])])
    >>> profit(t)
    8
    """
    return helper(t, False)

def helper(t, used_parent):
    if used_parent:
        return sum([helper(branch,False)for branch in branches(t)])
    else:
        used_label = label(t) +sum([helper(branch,True)for branch in branches(t)])
        no_label = sum([helper(branch, False) for branch in branches(t)])
        return max(used_label,no_label)
