/*
 * @lc app=leetcode id=678 lang=csharp
 *
 * [678] Valid Parenthesis String
 */

// @lc code=start
public class Solution {
    public bool CheckValidString(string s) {
        int openMax = 0;
        int openMin = 0;
        foreach (char c in s) {
            if (c == '(') {
                openMax++;
                openMin++;
            }
            if (c == ')') {
                openMax--;
                openMin--;
            }
            if (c == '*') {
                openMax++;
                openMin--;
            }
            if (openMax < 0) {
                return false;
            }
            openMin = Math.Max(0, openMin);
        }
        return openMin == 0;
    }
}

// @lc code=end

