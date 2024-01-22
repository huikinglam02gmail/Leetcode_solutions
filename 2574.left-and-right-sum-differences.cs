/*
 * @lc app=leetcode id=2574 lang=csharp
 *
 * [2574] Left and Right Sum Differences
 */

// @lc code=start
using System;
using System.Collections.Generic;

public class Solution
{
    /**
     * Prefix Sum
     */
    public int[] LeftRightDifference(int[] nums)
    {
        List<int> prefixSum = new List<int> { 0 };
        foreach (int num in nums)
        {
            prefixSum.Add(prefixSum[^1] + num);
        }

        List<int> result = new List<int>();
        for (int i = 0; i < nums.Length; i++)
        {
            result.Add(Math.Abs(prefixSum[^1] - prefixSum[i + 1] - prefixSum[i]));
        }

        return result.ToArray();
    }
}

// @lc code=end

