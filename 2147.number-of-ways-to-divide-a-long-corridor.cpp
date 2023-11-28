/*
 * @lc app=leetcode id=2147 lang=cpp
 *
 * [2147] Number of Ways to Divide a Long Corridor
 */

// @lc code=start
#include <string>

class Solution {
public:
    int numberOfWays(std::string corridor) {
        long long MOD = 1000000007;
        int n = corridor.length();
        int l = n, r = n, countS = 0;
        long long result = 1;

        for (int i = 0; i < n; i++) {
            if (corridor[i] == 'S') {
                countS++;
                if (countS % 2 == 1) {
                    r = i;
                } else {
                    l = i;
                }

                if (l < r) {
                    result *= r - l;
                    result %= MOD;
                }
            }
        }

        return (countS % 2 == 1 || countS == 0) ? 0 : static_cast<int>(result);
    }
};

// @lc code=end

