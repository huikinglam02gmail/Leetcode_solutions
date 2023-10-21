/*
 * @lc app=leetcode id=1953 lang=cpp
 *
 * [1953] Maximum Number of Weeks for Which You Can Work
 */

// @lc code=start
#include <vector>
#include <algorithm>

class Solution {
public:
    long long numberOfWeeks(std::vector<int>& milestones) {
        long long M = 0;
        long long S = 0;

        for (int milestone : milestones) {
            M = std::max(M, static_cast<long long>(milestone));
            S += milestone;
        }

        return (2 * M <= S) ? S : (2 * (S - M) + 1);
    }
};

// @lc code=end

