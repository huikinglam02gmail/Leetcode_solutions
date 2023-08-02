/*
 * @lc app=leetcode id=1830 lang=cpp
 *
 * [1830] Minimum Number of Operations to Make String Sorted
 */

// @lc code=start
#include <iostream>
#include <vector>

class Solution {
public:
    int makeStringSorted(std::string s) {
        const int MOD = 1000000007;
        int n = s.length();
        std::vector<long long> factorials(n + 1);
        factorials[0] = 1;
        for (int i = 1; i <= n; i++) {
            factorials[i] = (factorials[i - 1] * i) % MOD;
        }

        std::vector<long long> inv(n + 1);
        inv[0] = 1;
        for (int i = 1; i <= n; i++) {
            inv[i] = ModPow(factorials[i], MOD - 2, MOD);
        }

        long long result = 0;
        std::vector<long long> cnts(26, 0);
        for (int i = n - 1; i >= 0; i--) {
            int ind = s[i] - 'a';
            cnts[ind]++;
            long long current = 0;
            for (int j = 0; j < ind; j++) {
                current += cnts[j];
            }
            current = (current * factorials[n - 1 - i]) % MOD;
            for (int j = 0; j < 26; j++) {
                current = (current * inv[cnts[j]]) % MOD;
            }
            result = (result + current) % MOD;
        }
        return static_cast<int>(result);
    }

private:
    long long ModPow(long long x, long long y, long long mod) {
        long long result = 1;
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
};

// @lc code=end

