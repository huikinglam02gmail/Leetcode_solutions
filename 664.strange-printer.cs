/*
 * @lc app=leetcode id=664 lang=csharp
 *
 * [664] Strange Printer
 */

// @lc code=start
public class Solution {
    public int StrangePrinter(string s) {
        StringBuilder sb = new StringBuilder();
        foreach (char c in s) {
            if (sb.Length == 0 || c != sb[sb.Length - 1]) {
                sb.Append(c);
            }
        }
        string str = sb.ToString();
        int n = str.Length;
        int[,] dp = new int[n, n];
        
        for (int j = 0; j < n; j++) {
            for (int i = j; i >= 0; i--) {
                if (i == j) {
                    dp[i, j] = 1;
                }
                else if (i == j - 1) {
                    dp[i, j] = 2;
                }
                else {
                    dp[i, j] = 1 + dp[i + 1, j];
                    for (int k = i + 1; k <= j; k++) {
                        if (str[i] == str[k]) {
                            dp[i, j] = Math.Min(dp[i, j], dp[i + 1, k - 1] + dp[k, j]);
                        }
                    }
                }
            }
        }
        return dp[0, n - 1];
    }
}

// @lc code=end

