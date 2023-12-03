/*
 * @lc app=leetcode id=1266 lang=csharp
 *
 * [1266] Minimum Time Visiting All Points
 */

// @lc code=start
using System;
using System.Collections.Generic;

public class Solution {
    public int MinTimeToVisitAllPoints(int[][] points) {
        int result = 0;
        int n = points.Length;

        for (int i = 0; i < n - 1; i++) {
            int x1 = points[i][0];
            int y1 = points[i][1];
            int x2 = points[i + 1][0];
            int y2 = points[i + 1][1];

            result += Math.Max(Math.Abs(x1 - x2), Math.Abs(y1 - y2));
        }

        return result;
    }
}

// @lc code=end

