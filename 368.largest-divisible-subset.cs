/*
 * @lc app=leetcode id=368 lang=csharp
 *
 * [368] Largest Divisible Subset
 */

// @lc code=start
using System;
using System.Collections.Generic;
using System.Linq;

public class Solution {
    public IList<int> LargestDivisibleSubset(int[] nums) {
        Array.Sort(nums);
        List<List<int>> dp = new List<List<int>>();

        foreach (int num in nums) {
            dp.Add(new List<int> { num });
        }

        for (int i = 1; i < nums.Length; i++) {
            for (int j = 0; j < i; j++) {
                if (nums[i] % nums[j] == 0 && dp[i].Count < dp[j].Count + 1) {
                    dp[i] = new List<int>(dp[j]);
                    dp[i].Add(nums[i]);
                }
            }
        }

        int index = 0;
        int maxLength = 1;
        for (int i = 0; i < dp.Count; i++) {
            if (dp[i].Count > maxLength) {
                index = i;
                maxLength = dp[i].Count;
            }
        }

        return dp[index];
    }
}

// @lc code=end

