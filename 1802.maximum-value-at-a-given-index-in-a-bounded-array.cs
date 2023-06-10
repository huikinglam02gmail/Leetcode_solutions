/*
 * @lc app=leetcode id=1802 lang=csharp
 *
 * [1802] Maximum Value at a Given Index in a Bounded Array
 */

// @lc code=start
using System;
public class Solution
{
    public int MaxValue(int n, int index, int maxSum)
    {
        long left = 0;
        long right = maxSum + 1;
        
        while (left < right)
        {
            long k = left + (right - left) / 2;
            long S = k * k;
            S += Math.Max(0, index - k + 1);
            S += Math.Max(0, n - index - k);
            
            if (index - k + 1 < 0)
            {
                S -= (k - index - 1) * (k - index) / 2;
            }
            
            if (index + k - 1 >= n)
            {
                S -= (k - (n - index)) * (k - n + index + 1) / 2;
            }
            
            if (S <= maxSum)
            {
                left = k + 1;
            }
            else
            {
                right = k;
            }
        }
        
        return Convert.ToInt32(left - 1);
    }
}

// @lc code=end

