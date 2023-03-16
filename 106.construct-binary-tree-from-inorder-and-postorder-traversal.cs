/*
 * @lc app=leetcode id=106 lang=csharp
 *
 * [106] Construct Binary Tree from Inorder and Postorder Traversal
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
using System.Linq;
public class Solution 
{
    public TreeNode BuildTree(int[] inorder, int[] postorder) 
    {
        TreeNode root = null;
        if (postorder.Length > 0)
        {
            int rootVal = postorder[postorder.Length - 1];
            root = new TreeNode(rootVal);
            int left = inorder.TakeWhile(x => x != rootVal).Count();
            root.left = BuildTree(inorder.Take(left).ToArray(), postorder.Take(left).ToArray());
            root.right = BuildTree(inorder.Skip(left + 1).ToArray(), postorder.Skip(left).Take(postorder.Length - left - 1).ToArray());
        }    
        return root;
    }
}
// @lc code=end

