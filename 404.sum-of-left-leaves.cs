/*
 * @lc app=leetcode id=404 lang=csharp
 *
 * [404] Sum of Left Leaves
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
using System;
using System.Collections.Generic;

public class Solution {
    public int SumOfLeftLeaves(TreeNode root) {
        if (root == null)
            return 0;
        
        Queue<TreeNode> queue = new Queue<TreeNode>();
        queue.Enqueue(root);
        int result = 0;
        
        while (queue.Count > 0) {
            TreeNode node = queue.Dequeue();
            if (node.left != null) {
                queue.Enqueue(node.left);
                if (node.left.left == null && node.left.right == null)
                    result += node.left.val;
            }
            if (node.right != null)
                queue.Enqueue(node.right);
        }
        
        return result;
    }
}

// @lc code=end

