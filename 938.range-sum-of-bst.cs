/*
 * @lc app=leetcode id=938 lang=csharp
 *
 * [938] Range Sum of BST
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
    public int RangeSumBST(TreeNode root, int low, int high)
    {
        if (root == null)
        {
            return 0;
        }
        else if (root.val > low && root.val > high)
        {
            return RangeSumBST(root.left, low, high);
        }
        else if (root.val < low && root.val < high)
        {
            return RangeSumBST(root.right, low, high);
        }
        else
        {
            return root.val + RangeSumBST(root.left, low, high) + RangeSumBST(root.right, low, high);
        }
    }
}
// @lc code=end

