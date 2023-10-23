/*
 * @lc app=leetcode id=1955 lang=csharp
 *
 * [1955] Count Number of Special Subsequences
 */

// @lc code=start
public class Solution {
    public int CountSpecialSubsequences(int[] nums) {
        long[] prev = new long[3];
        long MOD = 1000000007;

        foreach (var num in nums) {
            long[] next = new long[3];

            for (int i = 0; i < 3; i++) {
                next[i] += prev[i];

                if (i == num) {
                    next[i] += prev[i];
                    if (i > 0) {
                        next[i] += prev[i - 1];
                    }
                }

                next[i] %= MOD;
            }

            if (num == 0) {
                next[num] += 1;
            }

            prev = next;
        }

        return Convert.ToInt32(prev[2]);
    }
}

// @lc code=end

