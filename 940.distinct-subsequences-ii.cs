/*
 * @lc app=leetcode id=940 lang=csharp
 *
 * [940] Distinct Subsequences II
 */

// @lc code=start
public class Solution {
    public int DistinctSubseqII(string s) {
        long[] dp = new long[26];
        long current = 0;
        long MOD = 1000000007;

        foreach (char c in s) {
            dp[c - 'a'] = (1 + current) % MOD;
            current = dp.Sum() % MOD;
        }

        return Convert.ToInt32(current);
    }
}

// @lc code=end

