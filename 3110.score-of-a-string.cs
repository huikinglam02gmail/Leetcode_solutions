/*
 * @lc app=leetcode id=3110 lang=csharp
 *
 * [3110] Score of a String
 */

// @lc code=start
public class Solution {
    public int ScoreOfString(string s) {
        int n = s.Length;
        int result = 0;
        for (int i = 0; i < n - 1; i++) {
            result += Math.Abs(s[i + 1] - s[i]);
        }
        return result;
    }
}

// @lc code=end

