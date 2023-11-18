/*
 * @lc app=leetcode id=1986 lang=cpp
 *
 * [1986] Minimum Number of Work Sessions to Finish the Tasks
 */

// @lc code=start
#include <vector>
#include <algorithm>

class Solution {
public:
    int minSessions(std::vector<int>& tasks, int sessionTime) {
        int n = tasks.size();
        std::vector<std::vector<int>> dp(1 << n, std::vector<int>(2, n));

        for (int i = 0; i < (1 << n); i++) {
            dp[i][0] = n;
            dp[i][1] = 0;
        }

        dp[(1 << n) - 1][0] = 1;
        dp[(1 << n) - 1][1] = sessionTime;

        for (int mask = (1 << n) - 1; mask >= 0; mask--) {
            for (int i = 0; i < n; i++) {
                if ((mask & (1 << i)) == 0) {
                    int cntSession = dp[mask ^ (1 << i)][0];
                    int remainTime = dp[mask ^ (1 << i)][1];

                    if (tasks[i] <= remainTime) {
                        remainTime -= tasks[i];
                    } else {
                        cntSession += 1;
                        remainTime = sessionTime - tasks[i];
                    }

                    if (cntSession < dp[mask][0] || (cntSession == dp[mask][0] && remainTime > dp[mask][1])) {
                        dp[mask][0] = cntSession;
                        dp[mask][1] = remainTime;
                    }
                }
            }
        }

        return dp[0][0];
    }
};

// @lc code=end

