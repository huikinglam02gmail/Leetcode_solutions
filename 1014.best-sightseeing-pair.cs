/*
 * @lc app=leetcode id=1014 lang=csharp
 *
 * [1014] Best Sightseeing Pair
 */

// @lc code=start
using System;

public class Solution {
    public int MaxScoreSightseeingPair(int[] values) {
        int n = values.Length;
        int maxSoFar = 0;
        int last = 0;

        for (int i = 1; i < n; i++) {
            int current = values[i - 1] + values[i] - 1;

            if (i > 1) {
                current = Math.Max(current, last - values[i - 1] + values[i] - 1);
            }

            last = current;
            maxSoFar = Math.Max(maxSoFar, last);
        }

        return maxSoFar;
    }
}

// @lc code=end

