/*
 * @lc app=leetcode id=958 lang=csharp
 *
 * [958] Check Completeness of a Binary Tree
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
    public bool IsCompleteTree(TreeNode root) 
    {
        Queue<object[]> queue = new Queue<object[]>();
        int total = 0;
        queue.Enqueue(new object[2] {root, 1});

        while (queue.Count > 0)
        {
            int n = queue.Count;
            for (int i = 0; i < n; i++)
            {
                object[] item = queue.Dequeue();
                total++;
                if (Convert.ToInt32(item[1]) != total)
                {
                    return false;
                }
                if ((item[0] as TreeNode).left != null)
                {
                    queue.Enqueue(new object[2]{(item[0] as TreeNode)?.left, 2*Convert.ToInt32(item[1])});
                }
                if ((item[0] as TreeNode).right != null)
                {
                    queue.Enqueue(new object[2]{(item[0] as TreeNode)?.right, 2*Convert.ToInt32(item[1]) + 1});
                }
            }
        }
        return true;
    }
}
// @lc code=end

