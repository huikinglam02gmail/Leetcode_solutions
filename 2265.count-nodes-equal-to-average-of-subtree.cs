/*
 * @lc app=leetcode id=2265 lang=csharp
 *
 * [2265] Count Nodes Equal to Average of Subtree
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
    private int result;

    /*
     * Keep track of subtree sum and number of nodes in subtree.
     */
    public int[] DFS(TreeNode node)
    {
        if (node == null)
        {
            return new int[] { 0, 0 };
        }
        else
        {
            int[] leftData = DFS(node.left);
            int[] rightData = DFS(node.right);
            int leftSum = leftData[0];
            int leftTotal = leftData[1];
            int rightSum = rightData[0];
            int rightTotal = rightData[1];

            if (node.val == (node.val + leftSum + rightSum) / (1 + leftTotal + rightTotal))
            {
                result++;
            }

            return new int[] { node.val + leftSum + rightSum, 1 + leftTotal + rightTotal };
        }
    }

    public int AverageOfSubtree(TreeNode root)
    {
        result = 0;
        DFS(root);
        return result;
    }
}

// @lc code=end

