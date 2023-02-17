/*
 * @lc app=leetcode id=783 lang=csharp
 *
 * [783] Minimum Distance Between BST Nodes
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
public class Solution 
{
    int minDiff = Int32.MaxValue / 2;
    int lastVal = Int32.MinValue / 2;
    public void dfs(TreeNode node)
    {
        if (node.left is not null)
        {
            dfs(node.left);
        }
        minDiff = Math.Min(minDiff, node.val - lastVal);
        lastVal = node.val;
        if (node.right is not null)
        {
            dfs(node.right);
        }
    }
    public int MinDiffInBST(TreeNode root) 
    {
        dfs(root);
        return minDiff;
    }
}
// @lc code=end

