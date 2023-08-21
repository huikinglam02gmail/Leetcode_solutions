/*
 * @lc app=leetcode id=459 lang=csharp
 *
 * [459] Repeated Substring Pattern
 */

// @lc code=start
public class Solution {
    public bool RepeatedSubstringPattern(string s) {
        for (int i = 1; i <= s.Length / 2; i++) {
            if (s.Length % i == 0 && s == string.Concat(Enumerable.Repeat(s.Substring(0, i), s.Length / i))) {
                return true;
            }
        }
        return false;
    }
}

// @lc code=end

