/*
 * @lc app=leetcode id=1578 lang=csharp
 *
 * [1578] Minimum Time to Make Rope Colorful
 */

// @lc code=start
using System;
using System.Collections.Generic;

public class Solution {
    public int MinCost(string colors, int[] neededTime) {
        int i = 0, j = 0, result = 0, n = colors.Length;
        
        while (i < n && j < n) {
            int S = 0, m = 0;
            while (j < n && colors[j] == colors[i]) {
                S += neededTime[j];
                m = Math.Max(m, neededTime[j]);
                j++;
            }
            result += S - m;
            i = j;
        }

        return result;
    }
}

// @lc code=end

