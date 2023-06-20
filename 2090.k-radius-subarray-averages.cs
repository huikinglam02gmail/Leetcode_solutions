/*
 * @lc app=leetcode id=2090 lang=csharp
 *
 * [2090] K Radius Subarray Averages
 */

// @lc code=start
using System;
using System.Collections.Generic;

public class Solution
{
    public int[] GetAverages(int[] nums, int k)
    {
        int n = nums.Length;
        int[] result = new int[n];
        for (int i = 0; i < n; i++)
        {
            result[i] = -1;
        }
        if (n >= 2 * k + 1)
        {
            long windowSum = nums.Select(x => Convert.ToInt64(x)).Take(2 * k + 1).Sum();
            int i = k;
            while (i <= n - k - 1)
            {
                result[i] = Convert.ToInt32(windowSum / Convert.ToInt64(2 * k + 1));
                windowSum -= Convert.ToInt64(nums[i - k]);
                if (i + k + 1 < n)
                {
                    windowSum += Convert.ToInt64(nums[i + k + 1]);
                }
                i++;
            }
        }
        return result;
    }
}

// @lc code=end

