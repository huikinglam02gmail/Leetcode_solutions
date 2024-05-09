/*
 * @lc app=leetcode id=3075 lang=csharp
 *
 * [3075] Maximize Happiness of Selected Children
 */

// @lc code=start
using System;

public class Solution {
    public long MaximumHappinessSum(int[] happiness, int k) {
        Array.Sort(happiness);
        int n = happiness.Length;
        long result = 0;
        for (int i = n - 1; i >= n - k; i--) {
            result += Math.Max(0, happiness[i] - (n - 1 - i));
        }
        return result;
    }
}

// @lc code=end

