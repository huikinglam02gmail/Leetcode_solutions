/*
 * @lc app=leetcode id=1609 lang=csharp
 *
 * [1609] Even Odd Tree
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
    public bool IsEvenOddTree(TreeNode root) 
    {
        int level = 0;
        Queue<TreeNode> queue = new Queue<TreeNode>();
        queue.Enqueue(root);
        int prev;
        while (queue.Count > 0)
        {
            if (level % 2 == 0)
            {
                prev = 0;
            }
            else
            {
                prev = 1000001;
            }
            int n = queue.Count;
            for (int i = 0; i < n; i++)
            {
                TreeNode node = queue.Dequeue();
                if ((level % 2 == 0 && (node.val <= prev || node.val % 2 == 0)) || (level % 2 == 1 && (node.val >= prev || node.val % 2 == 1)))
                {
                    return False;
                }
                if (node.left != null)
                {
                    queue.Enqueue(node.left);
                }
                if (node.right != null)
                {
                    queue.Enqueue(node.right);
                }
                prev = node.val;
            }
            level++;
        }  
        return true;  
    }
}
// @lc code=end

