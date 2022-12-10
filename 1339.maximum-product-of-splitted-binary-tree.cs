/*
 * @lc app=leetcode id=1339 lang=csharp
 *
 * [1339] Maximum Product of Splitted Binary Tree
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
    HashSet<long> STS = new HashSet<long>();

    public long dfs(TreeNode node)
    {
        if (node == null)
        {
            return 0;
        }
        long result = node.val + dfs(node.left) + dfs(node.right);
        STS.Add(result);
        return result;
    }
    public int MaxProduct(TreeNode root) 
    {
        long total = dfs(root);
        long MOD = 1000000007;
        long maxSoFar = 0;
        foreach (long item in STS)
        {
            maxSoFar = Math.Max(maxSoFar, item*(total - item));
        }
        return maxSoFar % MOD;
    }
}
// @lc code=end

