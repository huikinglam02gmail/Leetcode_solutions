/*
 * @lc app=leetcode id=1830 lang=csharp
 *
 * [1830] Minimum Number of Operations to Make String Sorted
 */

// @lc code=start
using System;
using System.Linq;

public class Solution {
    public int MakeStringSorted(string s) {
        const int MOD = 1000000007;
        int n = s.Length;
        long[] factorials = new long[n + 1];
        factorials[0] = 1;
        for (int i = 1; i <= n; i++) {
            factorials[i] = (factorials[i - 1] * i) % MOD;
        }

        long[] inv = new long[n + 1];
        inv[0] = 1;
        for (int i = 1; i <= n; i++) {
            inv[i] = ModPow(factorials[i], MOD - 2, MOD);
        }

        long result = 0;
        long[] cnts = new long[26];
        for (int i = n - 1; i >= 0; i--) {
            int ind = s[i] - 'a';
            cnts[ind]++;
            long current = cnts.Take(ind).Sum();
            current = (current * factorials[n - 1 - i]) % MOD;
            for (int j = 0; j < 26; j++) {
                current = (current * inv[(int)cnts[j]]) % MOD;
            }
            result = (result + current) % MOD;
        }
        return Convert.ToInt32(result);
    }

    private long ModPow(long x, long y, long mod) {
        long result = 1;
        x = x % mod;
        while (y > 0) {
            if (y % 2 == 1) {
                result = (result * x) % mod;
            }
            y >>= 1;
            x = (x * x) % mod;
        }
        return result;
    }
}

// @lc code=end

