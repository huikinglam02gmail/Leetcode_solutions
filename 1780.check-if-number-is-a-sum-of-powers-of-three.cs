/*
 * @lc app=leetcode id=1780 lang=csharp
 *
 * [1780] Check if Number is a Sum of Powers of Three
 */

// @lc code=start
using System;
using System.Collections.Generic;

public class Solution
{
    public bool CheckPowersOfThree(int n)
    {
        int thres = 0;
        while (Math.Pow(3, thres) <= n)
        {
            thres++;
        }

        int[] dp = new int[1 << thres];
        for (int j = 0; j < thres; j++)
        {
            dp[1 << j] = (int)Math.Pow(3, j);
        }

        for (int mask = 1; mask < (1 << thres); mask++)
        {
            string binMask = Convert.ToString(mask, 2);
            if (binMask[0] != '0')
            {
                dp[mask] = dp[1 << (binMask.Length - 1)] + dp[mask - (1 << (binMask.Length - 1))];
            }
        }

        return Array.IndexOf(dp, n) != -1;
    }
}

// @lc code=end

