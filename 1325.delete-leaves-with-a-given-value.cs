/*
 * @lc app=leetcode id=1325 lang=csharp
 *
 * [1325] Delete Leaves With a Given Value
 */

// @lc code=start
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     public int val;
 *     public TreeNode left;
 *     public TreeNode right;
 *     public TreeNode(int val=0, TreeNode left=null, TreeNode right=null) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
 // Definition for a binary tree node.
public class Solution {
    // Helper method to perform DFS and remove leaf nodes with the target value
    private TreeNode Dfs(TreeNode node, int target) {
        if (node == null) {
            return null;
        }

        node.left = Dfs(node.left, target);
        node.right = Dfs(node.right, target);

        if (node.left == null && node.right == null && node.val == target) {
            return null;
        } else {
            return node;
        }
    }

    public TreeNode RemoveLeafNodes(TreeNode root, int target) {
        return Dfs(root, target);
    }
}

// @lc code=end

