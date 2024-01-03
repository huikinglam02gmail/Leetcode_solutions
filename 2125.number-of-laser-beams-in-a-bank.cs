/*
 * @lc app=leetcode id=2125 lang=csharp
 *
 * [2125] Number of Laser Beams in a Bank
 */

// @lc code=start
using System;
using System.Collections.Generic;

public class Solution {
    /*
    Remove all rows with "0" * n
    Then for two consecutive rows, add multiples of counts together
    */
    public int NumberOfBeams(string[] bank) {
        int prev = 0, result = 0;
        foreach (var row in bank) {
            int cur = row.Count(c => c == '1');
            if (cur == 0) continue;
            result += prev * cur;
            prev = cur;
        }
        return result;
    }
}

// @lc code=end

