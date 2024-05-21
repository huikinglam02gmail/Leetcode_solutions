/*
 * @lc app=leetcode id=1863 lang=csharp
 *
 * [1863] Sum of All Subset XOR Totals
 */

// @lc code=start
using System;
using System.Collections.Generic;

public class Solution {
    public int SubsetXORSum(int[] nums) {
        int n = nums.Length;
        int[] dp = new int[1 << n];
        int j = 0;

        for (int i = 1; i < (1 << n); i++) {
            if (i == (1 << (j + 1))) j++;
            dp[i] = dp[i - (1 << j)] ^ nums[j];
        }

        int sum = 0;
        foreach (int val in dp) {
            sum += val;
        }

        return sum;
    }
}

// @lc code=end

