/*
 * @lc app=leetcode id=1829 lang=csharp
 *
 * [1829] Maximum XOR for Each Query
 */

// @lc code=start
using System;
using System.Collections.Generic;

public class Solution {
    public int[] GetMaximumXor(int[] nums, int maximumBit) {
        int XOR = 0;
        foreach (int num in nums) {
            XOR ^= num;
        }
        int n = nums.Length;
        int[] result = new int[n];
        for (int i = 0; i < n; i++) {
            result[i] = ((1 << maximumBit) - 1) ^ XOR;
            XOR ^= nums[n - i - 1];
        }
        return result;
    }
}

// @lc code=end

