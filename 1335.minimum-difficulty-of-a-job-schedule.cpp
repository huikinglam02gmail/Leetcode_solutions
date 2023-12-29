/*
 * @lc app=leetcode id=1335 lang=cpp
 *
 * [1335] Minimum Difficulty of a Job Schedule
 */

// @lc code=start
#include <vector>
#include <stack>
#include <algorithm>

class Solution {
public:
    int minDifficulty(std::vector<int>& jobDifficulty, int d) {
        int n = jobDifficulty.size();
        if (n < d) return -1;

        std::vector<int> dp(n, 1000000);

        for (int day = 0; day < d; day++) {
            std::stack<int> stack;
            std::vector<int> dpNew(n, 0);

            for (int i = day; i < n; i++) {
                // In the new day, we just do job i
                if (i == 0) {
                    dpNew[i] = jobDifficulty[i];
                } else {
                    dpNew[i] = dp[i - 1] + jobDifficulty[i];
                }

                // Try to incorporate more jobs into day i
                while (!stack.empty() && jobDifficulty[stack.top()] <= jobDifficulty[i]) {
                    int j = stack.top();
                    stack.pop();
                    dpNew[i] = std::min(dpNew[i], dpNew[j] - jobDifficulty[j] + jobDifficulty[i]);
                }

                if (!stack.empty()) {
                    dpNew[i] = std::min(dpNew[i], dpNew[stack.top()]);
                }

                stack.push(i);
            }

            dp = dpNew;
        }

        return dp[n - 1];
    }
};

// @lc code=end

