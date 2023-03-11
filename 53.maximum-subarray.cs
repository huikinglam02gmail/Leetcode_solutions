/*
 * @lc app=leetcode id=53 lang=csharp
 *
 * [53] Maximum Subarray
 */

// @lc code=start
using System;
public class Solution 
{
    public int MaxSubArray(int[] nums) 
    {
        int maxSoFar = Int32.MinValue;   
        int maxEndingHere = 0;
        int n = nums.Length;

        foreach (int num in nums)
        {
            maxEndingHere += num;
            maxSoFar = Math.Max(maxSoFar, maxEndingHere);
            maxEndingHere = Math.Max(0, maxEndingHere);
        } 
        return maxSoFar;
    }
}
// @lc code=end

