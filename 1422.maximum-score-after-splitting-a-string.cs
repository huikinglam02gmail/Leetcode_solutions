/*
 * @lc app=leetcode id=1422 lang=csharp
 *
 * [1422] Maximum Score After Splitting a String
 */

// @lc code=start
public class Solution {
    public int MaxScore(string s) {
        int n = s.Length;
        int score = 0;
        int zeros = 0;
        int totalZeros = s.Count(f => (f == '0'));
        for (int i = 0; i < n-1; i++)
        {
            if (s[i]=='0')
            {
                zeros += 1;
            }
            score = Math.Max(score, 2*zeros + n - totalZeros - i - 1);
        }
        return score;
    }
}
// @lc code=end

