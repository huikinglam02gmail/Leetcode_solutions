/*
 * @lc app=leetcode id=2760 lang=csharp
 *
 * [2760] Longest Even Odd Subarray With Threshold
 */

// @lc code=start
using System;
using System.Collections.Generic;

public class Solution {
    public int LongestAlternatingSubarray(int[] nums, int threshold) {
        int n = nums.Length;
        int result = 0;

        for (int i = 0; i < n; i++) {
            if (nums[i] % 2 == 0 && nums[i] <= threshold) {
                int j = i + 1;
                while (j < n && nums[j] % 2 != nums[j - 1] % 2 && nums[j] <= threshold) {
                    j++;
                }
                result = Math.Max(result, j - i);
            }
        }

        return result;
    }
}

// @lc code=end

