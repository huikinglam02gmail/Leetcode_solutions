/*
 * @lc app=leetcode id=1808 lang=csharp
 *
 * [1808] Maximize Number of Nice Divisors
 */

// @lc code=start
public class Solution {
    private long powMOD(long x, long a, long mod)
    {
        if (a == 1) return x;
        if (a == 0) return 1;
        long k1 = powMOD(x, a / 2, mod);
        if (a % 2 == 0) {
            return (k1 * k1) % mod;
        } else {
            return (k1*k1*x) % mod;
        }
    }

    public int MaxNiceDivisors(int primeFactors) {
        long mod = 1000000007;
        if (primeFactors == 1) {
            return 1;
        } else if (primeFactors == 2) {
            return 2;
        } else {
            long a = Convert.ToInt64(primeFactors / 3);
            long b = Convert.ToInt64(primeFactors % 3);
            if (b == 0) {
                return Convert.ToInt32(powMOD(3, a, mod));
            } else if (b == 1) {
                return Convert.ToInt32((powMOD(3, a - 1, mod) * 4) % mod);
            } else if (b == 2) {
                return Convert.ToInt32((powMOD(3, a, mod) * 2) % mod);
            }
        }
        return -1;
    }
}
// @lc code=end

