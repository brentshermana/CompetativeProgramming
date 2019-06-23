/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */

/**
My solution works ok, but interviewers will probably expect the "clever" stack solution,
which exploits specific properties of the inorder traversal to avoid remembering state.

Specifically, in inorder traversal, the three kinds of "movement" between one 'returned'
node and the next are:
1) Go down *all the way* to the left
2) Go up one (this is the only reason we need the stack)
3) Go down to right *once*

This is LeetCode's solution:

public class Solution {
    public List < Integer > inorderTraversal(TreeNode root) {
        List < Integer > res = new ArrayList < > ();
        Stack < TreeNode > stack = new Stack < > ();
        TreeNode curr = root;
        while (curr != null || !stack.isEmpty()) {
            while (curr != null) {
                stack.push(curr);
                curr = curr.left;
            }
            curr = stack.pop();
            res.add(curr.val);
            curr = curr.right;
        }
        return res;
    }
}
*/


class TreeNodeWithState {
    TreeNode node;
    int state;

    TreeNodeWithState(TreeNode node) {
        this.node = node;
        this.state = 0;
    }
}

class Solution {
    // Must Be Iterative!!!
    public List<Integer> inorderTraversal(TreeNode root) {
        Stack<TreeNodeWithState> stack = new Stack<TreeNodeWithState>();
        List<Integer> traversal = new ArrayList<Integer>();
        if (root != null) {
            stack.push(new TreeNodeWithState(root));
        }
        while (!stack.isEmpty()) {
            // state 0: push left child
            // state 1: 'visit' self
            // state 2: push right child
            // state 3: done, pop
            TreeNodeWithState n = stack.peek();
            switch (n.state++) {
                case 0:
                    if (n.node.left != null) {
                        stack.push(new TreeNodeWithState(n.node.left));
                    }
                    break;
                case 1:
                    traversal.add(n.node.val);
                    break;
                case 2:
                    if (n.node.right != null) {
                        stack.push(new TreeNodeWithState(n.node.right));
                    }
                    break;
                case 3:
                    stack.pop();
                    break;
            }
        }
        return traversal;
    }
}
