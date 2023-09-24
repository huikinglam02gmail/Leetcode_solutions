/*
 * @lc app=leetcode id=1915 lang=csharp
 *
 * [1915] Number of Wonderful Substrings
 */

// @lc code=start
public class Solution {
    public long WonderfulSubstrings(string word) {
        long current = 0;
        long[] dp = new long[1 << 10];
        dp[0] = 1;
        long result = 0;

        foreach (char c in word) {
            current ^= (1 << (c - 'a'));
            result += dp[current];

            for (int i = 0; i < 10; i++) {
                result += dp[current ^ (1 << i)];
            }

            dp[current]++;
        }

        return result;
    }
}

// @lc code=end

