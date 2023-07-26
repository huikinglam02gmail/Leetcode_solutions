/*
 * @lc app=leetcode id=1828 lang=csharp
 *
 * [1828] Queries on Number of Points Inside a Circle
 */

// @lc code=start
using System;
using System.Collections.Generic;

public class Solution {
    public int[] CountPoints(int[][] points, int[][] queries) {
        List<int> result = new List<int>();
        foreach (var query in queries) {
            int x = query[0];
            int y = query[1];
            int r = query[2];
            int count = 0;
            foreach (var point in points) {
                int x1 = point[0];
                int y1 = point[1];
                if ((x - x1) * (x - x1) + (y - y1) * (y - y1) <= r * r) {
                    count++;
                }
            }
            result.Add(count);
        }
        return result.ToArray();
    }
}

// @lc code=end

