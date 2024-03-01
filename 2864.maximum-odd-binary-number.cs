/*
 * @lc app=leetcode id=2864 lang=csharp
 *
 * [2864] Maximum Odd Binary Number
 */

// @lc code=start
public class Solution {
    public string MaximumOddBinaryNumber(string s) {
        int n = s.Length;
        int countOne = s.Count(c => c == '1');
        return new string('1', countOne - 1) + new string('0', n - countOne) + '1';
    }
}

// @lc code=end

