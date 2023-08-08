/*
 * @lc app=leetcode id=153 lang=csharp
 *
 * [153] Find Minimum in Rotated Sorted Array
 */

// @lc code=start
using System;
using System.Collections.Generic;

public class Solution
{
    public int FindMin(int[] nums)
    {
        int l = 0;
        int r = nums.Length;
        while (l < r - 1)
        {
            int mid = l + (r - l) / 2;
            if (nums[mid] > nums[l])
            {
                l = mid;
            }
            else
            {
                r = mid;
            }
        }
        return nums[(l + 1) % nums.Length];
    }
}


// @lc code=end

