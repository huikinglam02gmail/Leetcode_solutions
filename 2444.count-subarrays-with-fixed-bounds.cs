/*
 * @lc app=leetcode id=2444 lang=csharp
 *
 * [2444] Count Subarrays With Fixed Bounds
 */

// @lc code=start
using System;
public class Solution 
{
    public long CountSubarrays(int[] nums, int minK, int maxK) 
    {
        int jMax = -1;
        int jMin = -1;
        int jBad = -1;
        long result = 0;
        for (int j = 0; j < nums.Length; j++)
        {
            if (nums[j] < minK || nums[j] > maxK)
            {
                jBad = j;
            }
            if (nums[j] == minK)
            {
                jMin = j;
            }
            if (nums[j] == maxK)
            {
                jMax = j;
            }
            result += Math.Max(0, Math.Min(jMin, jMax) - jBad);
        }    
        return result;
    }
}
// @lc code=end

