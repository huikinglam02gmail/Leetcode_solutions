/*
 * @lc app=leetcode id=1884 lang=cpp
 *
 * [1884] Egg Drop With 2 Eggs and N Floors
 */

// @lc code=start
#include <vector>

class Solution {
public:
    int superEggDrop(int k, int n) {
        std::vector<std::vector<int>> dp(n + 1, std::vector<int>(k + 1, 0));

        for (int m = 1; m <= n; m++) {
            for (int K = 1; K <= k; K++) {
                dp[m][K] = dp[m - 1][K - 1] + dp[m - 1][K] + 1;
            }

            if (dp[m][k] >= n) {
                return m;
            }
        }

        return -1; // Handle invalid input
    }

    int twoEggDrop(int n) {
        return superEggDrop(2, n);
    }
};

// @lc code=end

