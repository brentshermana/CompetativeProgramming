# these are pytest tests!

import random

from advanced_tree import Tree, TreeWithParent, RangeIter

def random_tree(seed, n, tree_class, debug=False):
    vals = list(range(n))
    random.seed(seed)
    random.shuffle(vals)
    tree = tree_class()
    for v in vals:
        tree.add(v)
    if debug:
        print(vals)
    return tree

def test_next_highest():
    n = 100
    for seed in range(100):
        tree = random_tree(seed, n, Tree)
        for x in range(n-1):
            assert(tree.next_highest(x).val == x+1)
        assert(tree.next_highest(n-1) is None)

def test_next_highest_with_parent():
    n = 100
    for seed in range(100):
        tree = random_tree(seed, n, TreeWithParent)
        for x in range(n-1):
            assert(tree.next_highest(tree.get(x)).val == x+1)
        assert(tree.next_highest(tree.get(n-1)) is None)

def test_rangeiter():
    ranges = [(-1, 3), (0, 5), (40, 60), (95, 101)]
    n = 100
    for seed in range(100):
        tree = random_tree(seed, n, Tree, debug=True)
        for lo, hi in ranges:
            it = RangeIter(tree.root, lo, hi)
            for i in range(lo, hi+1):
                print("i: {}".format(i))
                # if the value's in the tree
                if i >= 0 and i < n:
                    # make sure our iterator hits it
                    assert(next(it).val == i)

            # ensure the iterator is done
            try:
                next(it)
                print("should have stopped!")
                assert(False)
            except StopIteration:
                pass
