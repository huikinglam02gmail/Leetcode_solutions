/*
 * @lc app=leetcode id=124 lang=csharp
 *
 * [124] Binary Tree Maximum Path Sum
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
    int result;
    public int traversal(TreeNode root)
    {
        if (root == null)
        {
            return Int32.MinValue;
        }
        else
        {
            int left = traversal(root.left);
            int right = traversal(root.right);
            int passThrough = root.val;
            int nonPassThrough = root.val + left + right;
            passThrough = Math.Max(passThrough, root.val + left);
            passThrough = Math.Max(passThrough, root.val + right);
            nonPassThrough = Math.Max(passThrough, left);
            nonPassThrough = Math.Max(passThrough, right);
            result = Math.Max(result, nonPassThrough);
            return passThrough;
        }
    }
    public int MaxPathSum(TreeNode root) 
    {
        result = Int32.MinValue;
        int rootVal = traversal(root);
        return Math.Max(root_val, result);   
    }
}
// @lc code=end

