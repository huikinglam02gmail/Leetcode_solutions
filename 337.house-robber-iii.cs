/*
 * @lc app=leetcode id=337 lang=csharp
 *
 * [337] House Robber III
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
    private Dictionary<Tuple<int, bool>, int> memo;

    public int dfs(TreeNode node, int nodeID, bool robThisNode)
    {
        Tuple<int, bool> key = new Tuple<int, bool>(nodeID, robThisNode);
        if (memo.ContainsKey(key))
        {
            return memo[key];
        }
        else
        {
            int result = 0;
            if (node != null)
            {
                if (robThisNode)
                {
                    result += node.val;
                    result += dfs(node.left, 2 * nodeID + 1, false);
                    result += dfs(node.right, 2 * nodeID + 2, false);
                }
                else
                {
                    result += Math.Max(dfs(node.left, 2 * nodeID + 1, false), dfs(node.left, 2 * nodeID + 1, true));
                     result += Math.Max(dfs(node.right, 2 * nodeID + 2, false), dfs(node.right, 2 * nodeID + 2, true));                   
                }
            }
            memo.Add(key, result);
            return result;
        }
    }

    public int Rob(TreeNode root) 
    {
        memo = new Dictionary<Tuple<int, bool>, int>();
        return Math.Max(dfs(root, 0, true), dfs(root, 0, false));
    }
}
// @lc code=end

