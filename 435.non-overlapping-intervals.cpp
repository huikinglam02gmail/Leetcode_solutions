/*
 * @lc app=leetcode id=435 lang=cpp
 *
 * [435] Non-overlapping Intervals
 */

// @lc code=start
#include <vector>
#include <algorithm>

class Solution {
public:
    /*
     * The minimum number of intervals you need to remove is equal to
     * n - the maximum length of non-overlapping intervals.
     * We can first sort intervals by the second index
     * (Earlier ending ones leave room for future ones to fill in).
     */

    int eraseOverlapIntervals(std::vector<std::vector<int>>& intervals) {
        std::sort(intervals.begin(), intervals.end(), [](const std::vector<int>& a, const std::vector<int>& b) {
            return a[1] < b[1] || (a[1] == b[1] && a[0] < b[0]);
        });
        int n = intervals.size();
        std::vector<std::vector<int>> result;
        int ans = 0;

        for (const auto& interval : intervals) {
            if (!result.empty() && interval[0] < result.back()[1]) {
                ans++;
            } else {
                result.push_back(interval);
            }
        }

        return ans;
    }
};

// @lc code=end

