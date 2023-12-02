/*
 * @lc app=leetcode id=2001 lang=csharp
 *
 * [2001] Number of Pairs of Interchangeable Rectangles
 */

// @lc code=start
using System;
using System.Collections.Generic;

public class Solution {
    public long InterchangeableRectangles(int[][] rectangles) {
        Dictionary<double, long> hashTable = new Dictionary<double, long>();
        long result = 0;

        foreach (var rectangle in rectangles) {
            double ratio = (double)rectangle[1] / rectangle[0];
            hashTable[ratio] = 1 + hashTable.GetValueOrDefault(ratio, 0);
        }

        foreach (var count in hashTable.Values) {
            result += count * (count - 1) / 2;
        }

        return result;
    }
}

// @lc code=end

