/*
 * @lc app=leetcode id=1335 lang=csharp
 *
 * [1335] Minimum Difficulty of a Job Schedule
 */

// @lc code=start
using System;
using System.Collections.Generic;

public class Solution {
    public int MinDifficulty(int[] jobDifficulty, int d) {
        int n = jobDifficulty.Length;
        if (n < d) return -1;

        int[] dp = new int[n];
        Array.Fill(dp, 1000000);
        for (int day = 0; day < d; day++) {
            Stack<int> stack = new Stack<int>();
            int[] dpNew = new int[n];

            for (int i = day; i < n; i++) {
                // In the new day, we just do job i
                if (i == 0) {
                    dpNew[i] = jobDifficulty[i];
                } else {
                    dpNew[i] = dp[i - 1] + jobDifficulty[i];
                }

                // Try to incorporate more jobs into day i
                while (stack.Count > 0 && jobDifficulty[stack.Peek()] <= jobDifficulty[i]) {
                    int j = stack.Pop();
                    dpNew[i] = Math.Min(dpNew[i], dpNew[j] - jobDifficulty[j] + jobDifficulty[i]);
                }

                if (stack.Count > 0) {
                    dpNew[i] = Math.Min(dpNew[i], dpNew[stack.Peek()]);
                }

                stack.Push(i);
            }

            dp = dpNew;
        }

        return dp[n - 1];
    }
}

// @lc code=end

