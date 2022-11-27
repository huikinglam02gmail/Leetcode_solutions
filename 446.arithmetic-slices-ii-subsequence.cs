/*
 * @lc app=leetcode id=446 lang=csharp
 *
 * [446] Arithmetic Slices II - Subsequence
 */

// @lc code=start
public class Solution 
{
    public int NumberOfArithmeticSlices(int[] nums) 
    {
        int n = nums.Length;
        if (n < 3)
        {
            return 0;
        }
        Dictionary<long,int>[] dp = new Dictionary<long,int>[n];
        dp[0] = new Dictionary<long,int>();
        int result = 0;
        for (int i = 1; i < n; i++)
        {
            dp[i] = new Dictionary<long,int>();
            for (int j = 0; j < i; j++)
            {
                long diff = (long) nums[i] - (long)nums[j];
                if (!dp[i].ContainsKey(diff))
                {
                    dp[i].Add(diff, 0);
                }
                dp[i][diff]++;
                if (dp[j].ContainsKey(diff))
                {
                    dp[i][diff] += dp[j][diff];
                    result += dp[j][diff];
                }             
            }
        }
        return result;
    }
}
// @lc code=end

