/*
 * @lc app=leetcode id=1161 lang=csharp
 *
 * [1161] Maximum Level Sum of a Binary Tree
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
public class Solution {
    /*
    BFS and keep track of maximum sum seen so far
    */
    public int MaxLevelSum(TreeNode root)
    {
        Queue<TreeNode> queue = new Queue<TreeNode>();
        int level = 1, maxLevel = -1;
        int maxSoFar = int.MinValue;
        queue.Enqueue(root);

        while (queue.Count > 0)
        {
            int total = 0;
            int queueLength = queue.Count;

            for (int i = 0; i < queueLength; i++)
            {
                TreeNode node = queue.Dequeue();
                total += node.val;

                if (node.left != null)
                    queue.Enqueue(node.left);

                if (node.right != null)
                    queue.Enqueue(node.right);
            }

            if (total > maxSoFar)
            {
                maxLevel = level;
                maxSoFar = total;
            }

            level++;
        }

        return maxLevel;
    }
}
// @lc code=end

