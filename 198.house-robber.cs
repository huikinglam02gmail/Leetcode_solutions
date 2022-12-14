/*
 * @lc app=leetcode id=198 lang=csharp
 *
 * [198] House Robber
 */

// @lc code=start
public class Solution 
{
    public int Rob(int[] nums) 
    {
        int n = nums.Length;
        if (n == 1)
        {
            return nums[0];
        }
        else if (n == 2)
        {
            return nums.Max(x => x);
        }
        else
        {
            int[] dp = new int[n];
            Array.Fill(dp, 0);
            dp[0] = nums[0];
            dp[1] = Math.Max(nums[0], nums[1]);
            for (int i = 2; i < n; i++)
            {
                dp[i] = Math.Max(nums[i] + dp[i-2], dp[i-1]);
            }
            return dp[n-1];            
        }
    }
}
// @lc code=end

