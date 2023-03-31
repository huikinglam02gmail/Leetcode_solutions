/*
 * @lc app=leetcode id=462 lang=csharp
 *
 * [462] Minimum Moves to Equal Array Elements II
 */

// @lc code=start
using System;
public class Solution 
{
    public int MinMoves2(int[] nums) 
    {
        Array.Sort(nums);
        int l = 0;
        int r = nums.Length - 1;
        int result = 0;
        while (l < r)
        {
            result += nums[r] - nums[l];
            r--;
            l++;
        }
        return result;
    }
}
// @lc code=end

