/*
 * @lc app=leetcode id=57 lang=cpp
 *
 * [57] Insert Interval
 */

// @lc code=start
#include <vector>
#include <algorithm>

using std::max;
using std::vector;

class Solution {
public:
    std::vector<std::vector<int>> insert(std::vector<std::vector<int>>& intervals, std::vector<int>& newInterval) {
        int lval = newInterval[0];
        int rval = newInterval[1];
        auto comp = [](const std::vector<int>& a, const std::vector<int>& b) {
            return a[1] < b[0];
        };
        auto l = std::lower_bound(intervals.begin(), intervals.end(), newInterval, comp) - intervals.begin();
        auto r = std::upper_bound(intervals.begin(), intervals.end(), newInterval, comp) - intervals.begin();

        if (l < intervals.size()) {
            lval = std::min(lval, intervals[l][0]);
        }
        if (r > 0) {
            rval = std::max(rval, intervals[r - 1][1]);
        }
        vector<vector<int>> result{};
        for (int i = 0; i < intervals.size(); ++i){
            if (i < l){
                result.push_back(intervals[i]);
            } else if (i == l)
            {
                result.push_back(vector<int> {lval, rval});
            }
            if (i >= r){
                result.push_back(intervals[i]);
            }
        }
        if (l == intervals.size()) result.push_back(newInterval);
        return result;
    }
};

// @lc code=end

