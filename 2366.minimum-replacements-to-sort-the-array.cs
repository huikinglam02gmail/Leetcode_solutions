/*
 * @lc app=leetcode id=2366 lang=csharp
 *
 * [2366] Minimum Replacements to Sort the Array
 */

// @lc code=start
using System;
using System.Collections.Generic;

public class Solution {
    public long CeilDiv(long i, long j) {
        return (i + j - 1) / j;
    }

    public long MinimumReplacement(int[] nums) {
        long remainder = nums[nums.Length - 1];
        int n = nums.Length;
        long result = 0;
        
        for (int i = n - 2; i >= 0; i--) {
            result += CeilDiv(nums[i], remainder) - 1;
            remainder = Convert.ToInt64(nums[i]) / CeilDiv(nums[i], remainder);
        }
        
        return result;
    }
}

// @lc code=end

