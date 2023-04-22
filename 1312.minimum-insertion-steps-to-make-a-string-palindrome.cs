/*
 * @lc app=leetcode id=1312 lang=csharp
 *
 * [1312] Minimum Insertion Steps to Make a String Palindrome
 */

// @lc code=start
using System.Linq;
using System;
public class Solution 
{
    public int LongestPalindromeSubseq(string s) 
    {
        int n = s.Length;
        int[][] dp = new int[n][];
        dp = dp.Select(x => Enumerable.Repeat(0, n).ToArray()).ToArray();
        for (int j = 0; j < n; j++)
        {
            for (int i = j; i >= 0; i--)
            {
                if (i == j)
                {
                    dp[i][j] = 1;
                }
                else
                {
                    dp[i][j] = Math.Max(dp[i][j - 1], dp[i + 1][j]);
                    if (s[i] == s[j])
                    {
                        dp[i][j] = Math.Max(dp[i][j], 2 + dp[i + 1][j - 1]);
                    }
                }
            }
        }
        return dp[0][n - 1];
    }

    public int MinInsertions(string s) 
    {
        return s.Length - LongestPalindromeSubseq(s);
    }
}
// @lc code=end

