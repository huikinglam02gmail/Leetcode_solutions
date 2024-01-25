/*
 * @lc app=leetcode id=1143 lang=csharp
 *
 * [1143] Longest Common Subsequence
 */

// @lc code=start
public class Solution {
    /**
     * Classic DP problem
     * dp[i][j] = LCS length between text1[:i] and text2[:j]
     */
    public int LongestCommonSubsequence(string text1, string text2) {
        int[,] dp = new int[text2.Length + 1, text1.Length + 1];
        
        for (int i = 1; i <= text2.Length; i++) {
            for (int j = 1; j <= text1.Length; j++) {
                dp[i, j] = Math.Max(dp[i, j - 1], dp[i - 1, j]);
                if (text1[j - 1] == text2[i - 1]) {
                    dp[i, j] = Math.Max(dp[i, j], dp[i - 1, j - 1] + 1);
                }
            }
        }
        
        return dp[text2.Length, text1.Length];
    }
}

// @lc code=end

