/*
 * @lc app=leetcode id=1987 lang=csharp
 *
 * [1987] Number of Unique Good Subsequences
 */

// @lc code=start
public class Solution {
    public int NumberOfUniqueGoodSubsequences(string binary) {
        long[] dp = new long[2];
        long current = 0;
        long MOD = 1000000007;
        int add1 = 0;

        foreach (char c in binary) {
            dp[c - '0'] = (c - '0' + current) % MOD;
            current = dp.Sum() % MOD;
            if (c == '0') {
                add1 = 1;
            }
        }

        return Convert.ToInt32(current + add1);
    }
}

// @lc code=end

