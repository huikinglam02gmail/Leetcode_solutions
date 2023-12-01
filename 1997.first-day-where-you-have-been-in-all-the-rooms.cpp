/*
 * @lc app=leetcode id=1997 lang=cpp
 *
 * [1997] First Day Where You Have Been in All the Rooms
 */

// @lc code=start
#include <vector>

class Solution {
private:
    const long long MOD = (long long)1000000007;

public:
    int firstDayBeenInAllRooms(std::vector<int>& nextVisit) {
        int n = nextVisit.size();
        std::vector<long long> dp(n, (long long)0);

        for (int i = 1; i < n; ++i) {
            dp[i] = (2 * dp[i - 1] + 2 - dp[nextVisit[i - 1]] + MOD) % MOD;
        }

        return (int)dp[n - 1];
    }
};

// @lc code=end

