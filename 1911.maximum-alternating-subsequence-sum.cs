/*
 * @lc app=leetcode id=1911 lang=csharp
 *
 * [1911] Maximum Alternating Subsequence Sum
 */

// @lc code=start
using System;
using System.Linq;
using System.Collections.Generic;

public class Solution {
    public long MaxAlternatingSum(int[] nums) {
        long result = nums[0];
        
        for (int i = 0; i < nums.Length - 1; i++) {
            result += Math.Max(0, nums[i + 1] - nums[i]);
        }
        
        return result;
    }
}

// @lc code=end

