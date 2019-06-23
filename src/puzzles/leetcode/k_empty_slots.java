// the values is 'bulbs' are 1-indexed
// you will return a day, those are also intdex 1 based
// return the minimum  day number that there exists two ON bulbs
// that have K bulbs between them that are off (can't be anything that's on between them)

// N^2 is trivial, just perform a scan after each 'turn'
// What if we populated a tree with the 'on' bulb indices? We would be able to access the next highest/lowest
// element in logn time, and insertions would be logn, so that's nlogn

// The algorithm for getting the next/prev element in a BST isn't obvious, but it comes
// up a lot. worth memorizing!
// See also: https://stackoverflow.com/questions/5471731/in-order-successor-in-binary-search-tree

class Node {
    Node parent;
    Node left;
    Node right;
    int val;

    Node(int i) { this.val = i; }

    // may return null!
    Node nextLargest() {
        if (this.right != null) {
            // smallest from right subtree
            Node tmp = this.right;
            while (tmp.left != null) {
                tmp = tmp.left;
            }
            return tmp;
        }
        else {
            // traverse upwards until we came from a left child
            Node cur = this.parent;
            Node prev = this;
            while (cur != null && cur.left != prev) {
                prev = cur;
                cur = cur.parent;
            }
            return cur; // may be null!
        }
    }

    // may return null!
    Node nextSmallest() {
        if (this.left != null) {
            // largest from left subtree
            Node tmp = this.left;
            while (tmp.right != null) {
                tmp = tmp.right;
            }
            return tmp;
        }
        else {
            // traverse upwards until we came from a right child
            Node cur = this.parent;
            Node prev = this;
            while (cur != null && cur.right != prev) {
                prev = cur;
                cur = cur.parent;
            }
            return cur; // may be null!
        }
    }
}

class BST {
    Node root = null;

    Node insert(int i) {
        if (root == null) {
            root = new Node(i);
            return root;
        }
        else {
            Node temp = root;
            while (true) {
                if (temp.val < i) {
                    if (temp.right == null) {
                        temp.right = new Node(i);
                        temp.right.parent = temp;
                        return temp.right;
                    }
                    else {
                        temp = temp.right;
                    }
                }
                else {
                    if (temp.left == null) {
                        temp.left = new Node(i);
                        temp.left.parent = temp;
                        return temp.left;
                    }
                    else {
                        temp = temp.left;
                    }
                }
            }
        }
    }
}

class Solution {
    // rather than tracking sets of contiguous 'off' bulbs, we track
    // the individual 'on' ones
    public int kEmptySlots(int[] bulbs, int K) {
        BST tree = new BST();
        for (int i = 0; i < bulbs.length; i++) {
            Node n = tree.insert(bulbs[i]);
            Node r = n.nextLargest();
            if (r != null && r.val - n.val-1 == K) {
                return i+1; // days are index 1 based
            }
            Node l = n.nextSmallest();
            if (l != null && n.val - l.val-1 == K) {
                return i+1; // days are index 1 based
            }
        }
        return -1;
    }
}
