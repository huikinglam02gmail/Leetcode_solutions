/*
 * @lc app=leetcode id=2678 lang=csharp
 *
 * [2678] Number of Senior Citizens
 */

// @lc code=start
using System;
using System.Collections.Generic;

public class Solution {
    public int CountSeniors(string[] details) {
        int result = 0;
        foreach (string detail in details) {
            if (int.Parse(detail.Substring(11, 2)) > 60) {
                result++;
            }
        }
        return result;
    }
}

// @lc code=end

