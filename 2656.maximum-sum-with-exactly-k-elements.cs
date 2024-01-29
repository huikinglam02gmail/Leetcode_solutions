/*
 * @lc app=leetcode id=2656 lang=csharp
 *
 * [2656] Maximum Sum With Exactly K Elements 
 */

// @lc code=start
using System;
using System.Collections.Generic;

public class Solution {
    public int MaximizeSum(int[] nums, int k) {
        return nums.Max() * k + k * (k - 1) / 2;
    }
}

// @lc code=end

