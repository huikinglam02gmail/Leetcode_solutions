/*
 * @lc app=leetcode id=312 lang=csharp
 *
 * [312] Burst Balloons
 */

// @lc code=start
using System;

public class Solution {
    public int MaxCoins(int[] nums) {
        int N = nums.Length;
        int[] extendedNums = new int[N + 2];
        Array.Copy(nums, 0, extendedNums, 1, N);
        extendedNums[0] = 1;
        extendedNums[N + 1] = 1;

        int[,] dp = new int[N + 2, N + 2];

        for (int j = 1; j <= N; j++) {
            dp[j, j] = extendedNums[j - 1] * extendedNums[j] * extendedNums[j + 1];
            for (int i = j - 1; i > 0; i--) {
                for (int last = i; last <= j; last++) {
                    dp[i, j] = Math.Max(dp[i, j], dp[i, last - 1] + extendedNums[i - 1] * extendedNums[last] * extendedNums[j + 1] + dp[last + 1, j]);
                }
            }
        }
        return dp[1, N];
    }
}

// @lc code=end

