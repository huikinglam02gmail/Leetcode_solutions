/*
 * @lc app=leetcode id=2331 lang=csharp
 *
 * [2331] Evaluate Boolean Binary Tree
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

public class Solution {
    /*
    Recursive function is your friend
    */
    public bool EvaluateTree(TreeNode root) {
        if (root.left == null && root.right == null) {
            return root.val != 0;
        }
        else {
            if (root.val == 2) {
                return EvaluateTree(root.left) || EvaluateTree(root.right);
            }
            else {
                return EvaluateTree(root.left) && EvaluateTree(root.right);
            }
        }
    }
}

// @lc code=end

