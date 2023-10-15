/*
 * @lc app=leetcode id=1269 lang=cpp
 *
 * [1269] Number of Ways to Stay in the Same Place After Some Steps
 */

// @lc code=start
/**
 * @lc app=leetcode id=1269 lang=cpp
 *
 * [1269] Number of Ways to Stay in the Same Place After Some Steps
 */

#include <vector>
using namespace std;

class Solution {
public:
    int numWays(int steps, int arrLen) {
        int finalLength = min(steps, arrLen);
        const long long MOD = 1000000007;

        vector<long long> dp(finalLength, 0);
        dp[0] = 1;

        for (int i = 0; i < steps; i++) {
            vector<long long> dpNew(finalLength, 0);

            for (int j = 0; j < finalLength; j++) {
                dpNew[j] = (dpNew[j] + dp[j]) % MOD;

                if (j < finalLength - 1) {
                    dpNew[j + 1] = (dpNew[j + 1] + dp[j]) % MOD;
                }

                if (j > 0) {
                    dpNew[j - 1] = (dpNew[j - 1] + dp[j]) % MOD;
                }
            }

            dp = dpNew;
        }

        return (int) (dp[0] % MOD);
    }
};

// @lc code=end

