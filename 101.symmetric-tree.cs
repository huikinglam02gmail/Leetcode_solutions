/*
 * @lc app=leetcode id=101 lang=csharp
 *
 * [101] Symmetric Tree
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
    public bool mirrorComparison(TreeNode node1, TreeNode node2)
    {
        if (node1 == null)
        {
            return node2 == null;
        }
        if (node2 == null)
        {
            return node1 == null;
        }
        if (node1.val != node2.val)
        {
            return false;
        }
        else
        {
            return mirrorComparison(node1.left, node2.right) && mirrorComparison(node1.right, node2.left);
        }
    }
    public bool IsSymmetric(TreeNode root) 
    {
        return mirrorComparison(root, root);
    }
}
// @lc code=end

