/*
 * @lc app=leetcode id=226 lang=csharp
 *
 * [226] Invert Binary Tree
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
    public TreeNode InvertTree(TreeNode root) 
    {
        if (root != null)
        {
            TreeNode temp = root.left;
            root.left = root.right;
            root.right = temp;
            root.left = InvertTree(root.left);
            root.right = InvertTree(root.right);
        }  
        return root;
    }
}
// @lc code=end

