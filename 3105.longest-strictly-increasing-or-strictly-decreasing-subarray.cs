/*
 * @lc app=leetcode id=3105 lang=csharp
 *
 * [3105] Longest Strictly Increasing or Strictly Decreasing Subarray
 */

// @lc code=start
using System;
using System.Collections.Generic;

public class Solution {
    /*
    Keep track of last num, result so far, current longest strictly increasing and strictly decreasing subarray ending at num
    */
    public int LongestMonotonicSubarray(int[] nums) {
        int currentIncr = 1, currentDecr = 1, result = 1, n = nums.Length;
        for (int i = 1; i < n; i++) {
            if (nums[i] > nums[i - 1]) {
                currentIncr++;
            } else {
                currentIncr = 1;
            }
            if (nums[i] < nums[i - 1]) {
                currentDecr++;
            } else {
                currentDecr = 1;
            }
            result = Math.Max(result, currentIncr);
            result = Math.Max(result, currentDecr);
        }
        return result;
    }
}

// @lc code=end

