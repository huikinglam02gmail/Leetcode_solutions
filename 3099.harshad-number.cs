/*
 * @lc app=leetcode id=3099 lang=csharp
 *
 * [3099] Harshad Number
 */

// @lc code=start
using System;

public class Solution {
    public int SumOfTheDigitsOfHarshadNumber(int x) {
        int S = 0;
        foreach (char c in x.ToString()) {
            S += int.Parse(c.ToString());
        }
        return (x % S == 0) ? S : -1;
    }
}

// @lc code=end

