// https://leetcode.com/problems/count-complete-tree-nodes/

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */

// we're told that the tree is complete, which is a big hint that
// we shouldn't just be counting all the nodes
// since the final row is going to be full from the left up until some point,
// we just need to figure out which point that is
// A guess is a traversal from the root to some leaf, which costs logn
// we can binary search across the possible values, which also costs logn
// so, our total runtime will be log(n)^2
class Solution {
    boolean checkPosition(TreeNode root, int i, int h) {
        // for an h of 2 and an i of 0, we would go left twice
        //                           1, we would go left, then right
        // for an h of 2 and an i of 2, we would go right, then left
        // ...
        // so what's the actual logic here?
        // this is just binary search, but on whether our i is greater than or less than 2^(h-1)

        // as an exercise we could also try this iteratively, but that might be overkill
        if (root == null) {
            return false;
        }
        if (h == 0) {
            return true;
        }
        int upperStart = (int) Math.pow(2, h-1);
        if (i < upperStart) {
            return checkPosition(root.left, i, h-1);
        }
        else {
            return checkPosition(root.right, i-upperStart, h-1);
        }
    }

    public int countNodes(TreeNode root) {
        if (root == null) {
            return 0;
        }

        int height = -1; // -1 instead of 0 because we're also incrementing at the root
        TreeNode cur = root;
        while (cur != null) {
            height ++;
            cur = cur.left;
        }

        int base = 0;
        int cap = (int) Math.pow(2, height);
        int highestSeen = -1; // should be set at least once!
        while (base < cap) {
            int mid = base + (cap-base)/2;
            if (checkPosition(root, mid, height)) {
                highestSeen = Math.max(highestSeen, mid);
                base = mid+1;
            }
            else {
                cap = mid;
            }
        }
        // if the tree were full, the number of nodes would be 2^(h+1) - 1
        // so, not including the final row, we have 2^(h)-1 nodes
        // We also add 1 to highestSeen because it's the index, not the number of nodes in the row
        return (int) Math.pow(2, height)-1 + highestSeen+1;
    }
}
