/*
 * @lc app=leetcode id=530 lang=csharp
 *
 * [530] Minimum Absolute Difference in BST
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
public class Solution 
{
    private int min_diff;
    private int last_node_val;

    public int GetMinimumDifference(TreeNode root)
    {
        min_diff = 100001;
        last_node_val = -100001;
        DFS(root);
        return min_diff;
    }

    private void DFS(TreeNode root)
    {
        if (root.left != null)
        {
            DFS(root.left);
        }

        min_diff = Math.Min(min_diff, root.val - last_node_val);
        last_node_val = root.val;

        if (root.right != null)
        {
            DFS(root.right);
        }
    }
}
// @lc code=end

