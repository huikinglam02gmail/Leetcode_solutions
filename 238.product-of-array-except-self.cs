/*
 * @lc app=leetcode id=238 lang=csharp
 *
 * [238] Product of Array Except Self
 */

// @lc code=start
using System;
using System.Collections.Generic;

public class Solution {
    public int[] ProductExceptSelf(int[] nums) {
        int n = nums.Length;
        int[] result = new int[n];
        
        for (int i = 0, prefix = 1; i < n; i++) {
            result[i] = prefix;
            prefix *= nums[i];
        }
        
        for (int i = n - 1, suffix = 1; i >= 0; i--) {
            result[i] *= suffix;
            suffix *= nums[i];
        }
        
        return result;
    }
}

// @lc code=end

