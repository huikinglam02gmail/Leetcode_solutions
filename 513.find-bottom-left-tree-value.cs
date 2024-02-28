/*
 * @lc app=leetcode id=513 lang=csharp
 *
 * [513] Find Bottom Left Tree Value
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

using System.Collections.Generic;

public class Solution {
    public int FindBottomLeftValue(TreeNode root) {
        Queue<TreeNode> queue = new Queue<TreeNode>();
        queue.Enqueue(root);
        
        int result = 0;
        while (queue.Count > 0) {
            TreeNode node = queue.Dequeue();
            result = node.val;
            if (node.right != null) {
                queue.Enqueue(node.right);
            }
            if (node.left != null) {
                queue.Enqueue(node.left);
            }
        }
        
        return result;
    }
}

// @lc code=end

