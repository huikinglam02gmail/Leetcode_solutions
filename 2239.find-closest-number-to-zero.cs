/*
 * @lc app=leetcode id=2239 lang=csharp
 *
 * [2239] Find Closest Number to Zero
 */

// @lc code=start
using System;
using System.Collections.Generic;

public class Solution {
    public int FindClosestNumber(int[] nums) {
        nums = nums.OrderBy(x => Math.Abs(x)).ThenBy(x=>-x).ToArray();
        return nums[0];
    }
}

// @lc code=end

