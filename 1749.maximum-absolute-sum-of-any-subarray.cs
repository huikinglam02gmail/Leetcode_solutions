/*
 * @lc app=leetcode id=1749 lang=csharp
 *
 * [1749] Maximum Absolute Sum of Any Subarray
 */

// @lc code=start
using System;

public class Solution
{
    /*
    -10^4 <= nums[i] <= 10^4
    if the maximum absolute sum subarray ends at nums[i]:
    if nums[i] < 0, we look for the minimum subarray ending at nums[i]
    if nums[i] > 0, we look for the maximum subarray ending at nums[i]
    So just do Kadane for maximum and minimum subarray, get max of the 2 abs of the 2 results
    */
    public int MaxSubArray(int[] nums)
    {
        int maxSoFar = int.MinValue;
        int maxEndingHere = 0;
        foreach (int num in nums)
        {
            maxEndingHere += num;
            maxSoFar = Math.Max(maxSoFar, maxEndingHere);
            maxEndingHere = Math.Max(0, maxEndingHere);
        }
        return maxSoFar;
    }

    public int MinSubArray(int[] nums)
    {
        int minSoFar = int.MaxValue;
        int minEndingHere = 0;
        foreach (int num in nums)
        {
            minEndingHere += num;
            minSoFar = Math.Min(minSoFar, minEndingHere);
            minEndingHere = Math.Min(0, minEndingHere);
        }
        return minSoFar;
    }

    public int MaxAbsoluteSum(int[] nums)
    {
        return Math.Max(Math.Abs(MaxSubArray(nums)), Math.Abs(MinSubArray(nums)));
    }
}

// @lc code=end

