/*
 * @lc app=leetcode id=2572 lang=csharp
 *
 * [2572] Count the Number of Square-Free Subsets
 */

// @lc code=start
using System.Collections.Generic;
using System;
public class Solution 
{
    Dictionary<int, int> primes = new Dictionary<int, int>(){
        {2, 0},
        {3, 1}, 
        {5, 2}, 
        {7, 3}, 
        {11, 4}, 
        {13, 5}, 
        {17, 6}, 
        {19, 7}, 
        {23, 8}, 
        {29, 9}
    };

    public int getNumMask(int num)
    {
        int mask = 0;
        while (num > 1)
        {
            foreach (int key in primes.Keys)
            {
                while (num % key == 0)
                {
                    if ((mask & (1 << primes[key])) == 0)
                    {
                        mask ^= (1 << primes[key]);
                        num /= key;
                    }
                    else
                    {
                        return -1;
                    }
                }
            }
        }
        return mask;
    }

    public int SquareFreeSubsets(int[] nums) 
    {
        int n = nums.Length;
        long MOD = 1000000007;
        long[][] dp = new long[n][];
        for (int i = 0; i < n; i++)
        {
            dp[i] = new long[1 << 10];
            Array.Fill(dp[i], 0);
        }

        long result = 0;
        for (int i = n - 1; i >= 0; i--)
        {
            int numMask = getNumMask(nums[i]);
            if (numMask >= 0)
            {
                dp[i][numMask] += 1;
                if (n == 1)
                {
                    return 1;
                }
            }
            if (i < n - 1)
            {
                for (int mask = 0; mask < (1 << 10); mask++)
                {
                    dp[i][mask] += dp[i + 1][mask];
                    if (numMask >= 0 && (((mask ^ numMask) & numMask) == 0))
                    {
                        dp[i][mask] += dp[i + 1][mask ^ numMask];
                    }
                    dp[i][mask] %= MOD;
                    if (i == 0)
                    {
                        result += dp[i][mask];
                        result %= MOD;
                    }
                }
            }
        }
        return Convert.ToInt32(result);
    }
}
// @lc code=end
