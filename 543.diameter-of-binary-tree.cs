/*
 * @lc app=leetcode id=543 lang=csharp
 *
 * [543] Diameter of Binary Tree
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
    private int result = 0;
    
    private int MaxDepth(TreeNode node) {
        if (node == null) return 0;
        int left = MaxDepth(node.left);
        int right = MaxDepth(node.right);
        result = Math.Max(result, left + right);
        return 1 + Math.Max(left, right);
    }

    public int DiameterOfBinaryTree(TreeNode root) {
        result = 0;
        MaxDepth(root);
        return result;
    }
}

// @lc code=end

