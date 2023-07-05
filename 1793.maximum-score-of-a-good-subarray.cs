/*
 * @lc app=leetcode id=1793 lang=csharp
 *
 * [1793] Maximum Score of a Good Subarray
 */

// @lc code=start
using System;

public class Solution
{
    public int MaximumScore(int[] nums, int k)
    {
        int result = nums[k];
        int minSoFar = nums[k];
        int i = k;
        int j = k;
        int n = nums.Length;

        while (i >= 0 && j <= n - 1)
        {
            minSoFar = Math.Min(minSoFar, nums[i]);
            minSoFar = Math.Min(minSoFar, nums[j]);
            result = Math.Max(result, minSoFar * (j - i + 1));

            if (i == 0)
            {
                j++;
            }
            else if (j == n - 1)
            {
                i--;
            }
            else if (nums[i - 1] < nums[j + 1])
            {
                j++;
            }
            else
            {
                i--;
            }
        }

        return result;
    }
}

// @lc code=end

