/*
 * @lc app=leetcode id=103 lang=csharp
 *
 * [103] Binary Tree Zigzag Level Order Traversal
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
 using System.Collections.Generic;
public class Solution 
{
    public IList<IList<int>> ZigzagLevelOrder(TreeNode root) 
    {
        Queue<TreeNode> queue = new Queue<TreeNode>();
        int level = 0;
        List<IList<int>> result = new List<IList<int>>();
        List<int> row = new List<int>(); 
        if (root != null)
        {
            queue.Enqueue(root);
            while(queue.Count > 0)
            {
                int l = queue.Count;
                row.Clear();
                for (int i = 0; i < l; i++)
                {
                    TreeNode node = queue.Dequeue();
                    row.Add(node.val);
                    if (node.left != null)
                    {
                        queue.Enqueue(node.left);
                    }
                    if (node.right != null)
                    {
                        queue.Enqueue(node.right);
                    }
                }
                if (level % 2 == 1)
                {
                    row.Reverse();
                }
                result.Add(new List<int>(row));
                level++;
            }
        }
        return result;
    }
}
// @lc code=end

