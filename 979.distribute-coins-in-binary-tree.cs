/*
 * @lc app=leetcode id=979 lang=csharp
 *
 * [979] Distribute Coins in Binary Tree
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
public class Solution {
    private int result;

    // We know the final state: node.val = 1 for all nodes.
    // Now let's think about the "flux" of coins between parent and its children
    // And define that to be the return value of the DFS function
    // If positive: coins will be going back to its parent
    // If negative: coins will be going from its parent    

    private int Dfs(TreeNode node) {
        if (node == null) return 0;
        int left = Dfs(node.left);
        int right = Dfs(node.right);
        result += Math.Abs(left) + Math.Abs(right);
        return node.val + left + right - 1;
    }

    public int DistributeCoins(TreeNode root) {
        result = 0;
        Dfs(root);
        return result;
    }
}

// @lc code=end

