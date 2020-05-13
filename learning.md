# Specific Problems

* TODO: Understand the "Median of Two Sorted Arrays" solution!

* Interval-based tree problems are hard for me, practice!
  * Trick: to check for overlap, the condition is simple:
    is_overlap = a.start < b.end and a.end > b.start
    * this isn't super obvious, I've written more complicated
      conditions to check this in the past

* TODO: practice specific binary search variants:
  * find leftmost duplicate of a value
  * find rightmost duplicate of a value
  * find value, or the closest value that's higher if not present
  * find value, or the closest value that's lower if not present

# Specific Data Structures, Algorithms

* Trie
  * I know what a trie is, and am good at consistently identifying
    good use cases for it
  * I am NOT good ot coding those solutions succinctly! For most problems
    you only need a dict to represent each node -- it's not worth
    defining classes with member functions!

* Union-Find
  * This only applies to a (relatively) small subset of problems, but it's really
    hard to solve problems that are optimally solved with union-find any other way
  * Also, it's really easy to implement once you know it
  * Find(x) -> returns the root of the subset x belongs to
    * Path Compression:
      * Optimize the structure of the tree by pointing the node directly to
        the parent after the result has been calculated!
      * See Wikipedia for an example!
  * Union(x, y) -> ensures x, y are members of the same set. If they aren't,
                   makes one set's root the child of the other's
    * Delegates to Find() for getting the roots
    * Can also optimize through union-by-size or union-by-rank to minimize
      the height of the resulting tree, but that's not necessary to get
      a pretty fast implementation. Also, these implementations are tedious
      because it's annoying to have to track the rank/size of each node (?)
       * Although, maybe it isn't hard. You only care about the size/rank
         of root nodes, after all. once a node isn't a root, it doesn't matter.
         You would only need to update the value when running Union()


* Tree Stuff:
  * Basic tree algorithms are easy!
  * I have trouble with tree problems which require lots of math to find a solution
    * eg count_complete_tree_nodes

* Advanced Tree Stuff:
  * Fetching items from a BST is easy. Other more advanced tasks such as querying a range,
    getting the next highest node or next lowest node, are really hard.
    * I originally wanted to use such algorithms for the leetcode problem "My Calendar I"
      and its variants, but ran out of time. I just need to become more familiar with them!
    * My practice for these concepts is in `src/algorithms/tree/advanced_tree.py`

* Array Problems
  * These are hard! I need more practice!

* Greedy Strategies
  * I AM BAD AT THIS. It's really hard to identify when a greedy strategy is
    optimal sometimes, and it's always possible to approach a greedy problem
    with another technique, to lesser success
  * ask yourself:
    * "do other techniques seem infeasible"?

* Dynamic Programming
  * I'm pretty good at it, this is just a back to basics review:
    * Figure out how to phrase the problem as a building up from subproblems to bigger
      problems ( e.g. A[i] = A[i-1] + A[i+1] )
    * Figure out how to iterate through the problems so that subproblems are solved
      before the bigger problems
    * What subproblem solutions, if any, can be thrown out after they're used? This
      improves memory performance

* Search Sequence for Subsequence
  * I was presented "find a string in a substring", but this is a pretty general
    set of problems and worth reviewing
    * More methods: https://en.wikipedia.org/wiki/String-searching_algorithm#Single-pattern_algorithms
    * Rabin-Karp: use a rolling hash
      * bad rolling hash: sum of each element of the series
    * Knuth Morris Pratt: like naive, but use info from failures to skip forward
      * really tedious, TODO study later!



* Bit Manipulation
  * single_number.py
  * sometimes bit manipulation gives the BEST runtime complexity! It's not ok
  * to not know it!
  * I REALLY need to practice this!


TODO: review topological sort, union find, segment trees, balanced trees
TODO: review all this stuff! https://www.geeksforgeeks.org/top-10-algorithms-in-interview-questions/
