/*
 * @lc app=leetcode id=2707 lang=csharp
 *
 * [2707] Extra Characters in a String
 */

// @lc code=start
using System;

public class Solution
{
    /*
    1 <= s.Length <= 50
    1 <= dictionary.Length <= 50
    1 <= dictionary[i].Length <= 50
    dp[i] = minimum number of extra characters left over if you break up s[i:] optimally
    dp[i] = Math.Min(1 + dp[j] if s[i:j] is not inside dictionary;
                    dp[j] if s[i:j] is inside dictionary)
    */
    public int MinExtraChar(string s, string[] dictionary)
    {
        HashSet<string> dictionarySet = new HashSet<string>(dictionary);
        int n = s.Length;
        int[] dp = new int[n + 1];

        for (int i = 0; i <= n; i++)
        {
            dp[i] = n;
        }

        dp[n] = 0;

        for (int i = n - 1; i >= 0; i--)
        {
            for (int j = i + 1; j <= n; j++)
            {
                if (!dictionarySet.Contains(s.Substring(i, j - i)))
                {
                    dp[i] = Math.Min(dp[i], j - i + dp[j]);
                }
                else
                {
                    dp[i] = Math.Min(dp[i], dp[j]);
                }
            }
        }

        return dp[0];
    }
}


// @lc code=end

