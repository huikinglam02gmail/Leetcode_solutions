/*
 * @lc app=leetcode id=70 lang=csharp
 *
 * [70] Climbing Stairs
 */

// @lc code=start
public class Solution 
{
    public int ClimbStairs(int n)
    {
        if (n == 1)
        {
            return 1;
        }    
        if (n == 2)
        {
            return 2;
        }
        int [] dp = new int[n];
        Array.Fill(dp, 0);
        dp[0] = 1;
        dp[1] = 2;
        for (int i = 2; i < n; i++)
        {
            dp[i] += dp[i-1];
            dp[i] += dp[i-2];
        }
        return dp[n-1];
    }
}
// @lc code=end

