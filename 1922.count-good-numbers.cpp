/*
 * @lc app=leetcode id=1922 lang=cpp
 *
 * [1922] Count Good Numbers
 */

// @lc code=start
class Solution {
public:
    int countGoodNumbers(long long n) {
        const int MOD = 1e9 + 7;
        long long result = modPow(20, n / 2, MOD);
        if (n % 2 == 1) {
            result = (result * 5) % MOD;
        }
        return static_cast<int>(result);
    }

private:
    long long modPow(long long x, long long n, int mod) {
        long long result = 1;
        while (n > 0) {
            if (n % 2 == 1) {
                result = (result * x) % mod;
            }
            x = (x * x) % mod;
            n /= 2;
        }
        return result;
    }
};

// @lc code=end

