/*
 * @lc app=leetcode id=1372 lang=csharp
 *
 * [1372] Longest ZigZag Path in a Binary Tree
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
    public int[] zigzag(TreeNode node)
    {
        int[] res = new int[2] { 0, 0 };
        if (node.left != null)
        {
            res[0] = 1 + zigzag(node.left)[1];
        }
        if (node.right != null)
        {
            res[1] = 1 + zigzag(node.right)[0];            
        }
        result = Math.Max(result, res[0]);
        result = Math.Max(result, res[1]);
        return res;
    }

    public int LongestZigZag(TreeNode root) 
    {
        result = 0;
        int[] res = zigzag(root);
        return result;
    }
}
// @lc code=end

