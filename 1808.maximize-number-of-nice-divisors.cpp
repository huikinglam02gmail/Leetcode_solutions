/*
 * @lc app=leetcode id=1808 lang=cpp
 *
 * [1808] Maximize Number of Nice Divisors
 */

// @lc code=start
class Solution {
private:
    long powMOD(long x, long a, long mod) {
        if (a == 1) return x;
        if (a == 0) return 1;
        long k1 = powMOD(x, a / 2, mod);
        if (a % 2 == 0) {
            return (k1 * k1) % mod;
        } else {
            return (k1 * k1 * x) % mod;
        }
    }

public:
    int maxNiceDivisors(int primeFactors) {
        long mod = 1000000007;
        if (primeFactors == 1) {
            return 1;
        } else if (primeFactors == 2) {
            return 2;
        } else {
            long a = static_cast<long>(primeFactors / 3);
            long b = static_cast<long>(primeFactors % 3);
            if (b == 0) {
                return static_cast<int>(powMOD(3, a, mod));
            } else if (b == 1) {
                return static_cast<int>((powMOD(3, a - 1, mod) * 4) % mod);
            } else if (b == 2) {
                return static_cast<int>((powMOD(3, a, mod) * 2) % mod);
            }
        }
        return -1;
    }
};
// @lc code=end

