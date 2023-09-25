/*
 * @lc app=leetcode id=1922 lang=csharp
 *
 * [1922] Count Good Numbers
 */

// @lc code=start
public class Solution {
    public int CountGoodNumbers(long n) {
        long MOD = (long)Math.Pow(10, 9) + 7;
        long result = ModPow(20, n / 2, MOD);
        if (n % 2 == 1) {
            result *= 5;
            result %= MOD;
        }
        return (int)result;
    }
    
    private long ModPow(long x, long n, long mod) {
        long result = 1;
        while (n > 0) {
            if (n % 2 == 1) {
                result = (result * x) % mod;
            }
            x = (x * x) % mod;
            n /= 2;
        }
        return result;
    }
}

// @lc code=end

