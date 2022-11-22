/*
 * @lc app=leetcode id=1483 lang=csharp
 *
 * [1483] Kth Ancestor of a Tree Node
 */

// @lc code=start
public class TreeAncestor 
{
    int[][] dp;
    public TreeAncestor(int n, int[] parent) 
    {
        dp = new int[n][];
        for (int i = 0; i < n; i++)
        {
            dp[i] = new int[16];
            Array.Fill(dp[i], -1);
        }
        for (int j = 0; j < 16; j++)
        {
            for (int i = 0; i < n; i++)
            {
                if (j == 0)
                {
                    dp[i][j] = parent[i];
                }
                else if (dp[i][j-1] >= 0)
                {
                    dp[i][j] = dp[dp[i][j-1]][j-1];
                }
            }
        }
    }
    
    public int GetKthAncestor(int node, int k) 
    {
        int i = 0;
        while (k > 0 && node >= 0)
        {
            if ((k & (1<<i)) != 0)
            {
                node = dp[node][i];
                k -= (1<<i);
            }
            i++;
        }
        return node;
    }
}

/**
 * Your TreeAncestor object will be instantiated and called as such:
 * TreeAncestor obj = new TreeAncestor(n, parent);
 * int param_1 = obj.GetKthAncestor(node,k);
 */
// @lc code=end

