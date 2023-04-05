/*
 * @lc app=leetcode id=2439 lang=csharp
 *
 * [2439] Minimize Maximum of Array
 */

// @lc code=start
using System.Linq;
using System;
public class Solution 
{
    public int MinimizeArrayValue(int[] nums) 
    {
        long l = Convert.ToInt64(nums.Min());
        long r = Convert.ToInt64(nums.Max());
        int n = nums.Length;
        while (l < r)
        {
            long mid = l + (r - l) / 2;
            long current = 0;
            for (int i = n - 1; i > 0; i--)
            {
                current = Math.Max(0, nums[i] + current - mid);
            }
            if (nums[0]+ current > mid)
            {
                l = mid + 1;
            }
            else
            {
                r = mid;
            }
        }
        return Convert.ToInt32(l);
    }
}
// @lc code=end

