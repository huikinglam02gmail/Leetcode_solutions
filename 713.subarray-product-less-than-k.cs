/*
 * @lc app=leetcode id=713 lang=csharp
 *
 * [713] Subarray Product Less Than K
 */

// @lc code=start
using System;

public class Solution {
    public int NumSubarrayProductLessThanK(int[] nums, int k) {
        if (k <= 1) return 0;
        int left = 0;
        int result = 0;
        int product = 1;
        for (int right = 0; right < nums.Length; right++) {
            product *= nums[right];
            while (product >= k) {
                product /= nums[left];
                left++;
            }
            result += right - left + 1;
        }
        return result;
    }
}

// @lc code=end

