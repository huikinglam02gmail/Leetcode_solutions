/*
 * @lc app=leetcode id=222 lang=csharp
 *
 * [222] Count Complete Tree Nodes
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
    public int height(TreeNode node)
    {
        int count = 0;
        while (!(node.left is null))
        {
            count += 1;
            node = node.left;
        }
        return count;
    }
    public int CountNodes(TreeNode root) 
    {
        if (root is null)
        {
            return 0;
        }
        if (root.left is null)
        {
            return 1;
        }
        if (root.right is null)
        {
            return 2;
        }
        int leftHeight = height(root.left);
        int rightHeight = height(root.right);
        int counter = 1;
        if (leftHeight == rightHeight)
        {
            for (int i = 0; i < leftHeight + 1; i++)
            {
                counter += (int) Math.Pow((double) 2, (double) i);
            }
            return counter + CountNodes(root.right);
        }
        else
        {
            for (int i = 0; i < rightHeight + 1; i++)
            {
                counter += (int) Math.Pow((double) 2, (double) i);
            }
            return counter + CountNodes(root.left);            
        }
    }
}
// @lc code=end

