/*
 * @lc app=leetcode id=662 lang=csharp
 *
 * [662] Maximum Width of Binary Tree
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
 using System.Collections.Generic;
 using System;
public class Solution 
{
    public int WidthOfBinaryTree(TreeNode root) 
    {
        Queue<object[]> queue = new Queue<object[]>();
        queue.Enqueue(new object[2]{root, 0});
        long maxWidth = 0;
        while (queue.Count > 0)
        {
            long maxPos = Int64.MinValue;
            long minPos = Int64.MaxValue;
            int n = queue.Count;
            for (int i = 0; i < n; i++)
            {
                object[] item = queue.Dequeue();
                long pos = Convert.ToInt64(item[1]);
                maxPos = Math.Max(pos, maxPos);
                minPos = Math.Min(pos, minPos);
                if (((TreeNode)item[0]).left != null)
                {
                    queue.Enqueue(new object[2]{((TreeNode)item[0]).left, 2 * pos});
                }
                if (((TreeNode)item[0]).right != null)
                {
                    queue.Enqueue(new object[2]{((TreeNode)item[0]).right, 2 * pos + 1});
                }
            }
            maxWidth = Math.Max(maxWidth, maxPos - minPos + 1);
        }   
        return Convert.ToInt32(maxWidth); 
    }
}
// @lc code=end

