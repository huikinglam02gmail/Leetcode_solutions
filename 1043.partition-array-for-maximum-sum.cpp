/*
 * @lc app=leetcode id=1043 lang=cpp
 *
 * [1043] Partition Array for Maximum Sum
 */

// @lc code=start
#include <vector>
#include <algorithm>

class Solution {
public:
    int maxSumAfterPartitioning(std::vector<int>& arr, int k) {
        int n = arr.size();
        std::vector<int> dp(n + 1, 0);

        for (int i = 1; i <= n; i++) {
            int currMax = 0;
            for (int j = i - 1; j > std::max(i - k - 1, -1); j--) {
                currMax = std::max(currMax, arr[j]);
                dp[i] = std::max(dp[i], dp[j] + (i - j) * currMax);
            }
        }

        return dp[n];
    }
};


// @lc code=end

