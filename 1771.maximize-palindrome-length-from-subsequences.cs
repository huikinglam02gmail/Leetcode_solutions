/*
 * @lc app=leetcode id=1771 lang=csharp
 *
 * [1771] Maximize Palindrome Length From Subsequences
 */

// @lc code=start
using System;
public class Solution
{
    /*
    First thing we should notice: the longest palindrome possible, must start at word1 and end at word2, and should be the same character.
    Remember the final product is always a subsequence of word1 + word2. We want to find the length of longest palindrome formed from that. We know how to solve Leetcode 516. Longest Palindromic Subsequence. In here, if word1[i] == word2[j], we ask for the longest palindromic subsequence of (word1 + word2)[i + 1: m + j]
    */
    public int LongestPalindrome(string word1, string word2)
    {
        string s = word1 + word2;
        int m = word1.Length;
        int[,] dp = new int[s.Length, s.Length];
        int result = 0;
        
        for (int j = 0; j < s.Length; j++)
        {
            for (int i = j; i >= 0; i--)
            {
                if (i == j)
                {
                    dp[i, j] = 1;
                }
                else
                {
                    dp[i, j] = Math.Max(dp[i, j - 1], dp[i + 1, j]);
                    if (s[i] == s[j])
                    {
                        dp[i, j] = Math.Max(dp[i, j], 2 + dp[i + 1, j - 1]);
                        if (i < m && j >= m)
                        {
                            result = Math.Max(result, dp[i, j]);
                        }
                    }
                }
            }
        }
        
        return result;
    }
}

// @lc code=end

