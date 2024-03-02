/*
 * @lc app=leetcode id=3010 lang=csharp
 *
 * [3010] Divide an Array Into Subarrays With Minimum Cost I
 */

// @lc code=start
using System;
using System.Collections.Generic;
using System.Linq;

public class Solution {
    public int MinimumCost(int[] nums) {
        Array.Sort(nums, 1, nums.Length - 1);
        return nums[0] + nums[1] + nums[2];
    }
}

// @lc code=end

