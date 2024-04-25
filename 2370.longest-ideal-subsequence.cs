/*
 * @lc app=leetcode id=2370 lang=csharp
 *
 * [2370] Longest Ideal Subsequence
 */

// @lc code=start
using System;

public class Solution {
    public int LongestIdealString(string s, int k) {
        int[] dp = new int[26];
        foreach (char c in s) {
            int index = c - 'a';
            int curr = 0;
            for (int i = index - k; i <= index + k; i++) {
                if (0 <= i && i < 26) curr = Math.Max(curr, dp[i] + 1);
            }
            dp[index] = curr;
        }
        int maxCount = 0;
        foreach (int count in dp) {
            maxCount = Math.Max(maxCount, count);
        }
        return maxCount;
    }
}

// @lc code=end

