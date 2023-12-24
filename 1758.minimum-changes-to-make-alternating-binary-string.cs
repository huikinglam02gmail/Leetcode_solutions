/*
 * @lc app=leetcode id=1758 lang=csharp
 *
 * [1758] Minimum Changes To Make Alternating Binary String
 */

// @lc code=start
public class Solution {
    public int MinOperations(string s) {
        int[] S = { 0, 0 };
        for (int i = 0; i < s.Length; i++) {
            S[1 - i % 2 - (int)Math.Pow(-1, i % 2) * (s[i] - '0')]++;
        }
        return Math.Min(S[0], S[1]);
    }
}

// @lc code=end

