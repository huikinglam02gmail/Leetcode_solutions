/*
 * @lc app=leetcode id=647 lang=csharp
 *
 * [647] Palindromic Substrings
 */

// @lc code=start
public class Solution {
    public int CountSubstrings(string s) {
        bool[,] dp = new bool[s.Length, s.Length];
        int count = 0;
        
        for (int j = 0; j < s.Length; j++) {
            for (int i = j; i >= 0; i--) {
                dp[i, j] = s[i] == s[j];
                if (i + 1 >= 0 && j - 1 >= 0 && i + 1 <= j - 1) {
                    dp[i, j] &= dp[i + 1, j - 1];
                }
                if (dp[i, j]) {
                    count++;
                }
            }
        }
        
        return count;
    }
}

// @lc code=end

