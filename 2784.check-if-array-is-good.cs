/*
 * @lc app=leetcode id=2784 lang=csharp
 *
 * [2784] Check if Array is Good
 */

// @lc code=start
using System;
using System.Collections.Generic;

public class Solution {
    public bool IsGood(int[] nums) {
        int n = nums.Length;
        Array.Sort(nums);

        for (int i = 0; i < n - 1; i++) {
            if (nums[i] != i + 1) {
                return false;
            }
        }

        return nums[n - 1] == n - 1;
    }
}

// @lc code=end

