/*
 * @lc app=leetcode id=1936 lang=cpp
 *
 * [1936] Add Minimum Number of Rungs
 */

// @lc code=start
#include <vector>
#include <algorithm>

class Solution {
public:
    int insertRungs(int diff, int dist) {
        int result = diff / dist;
        if (diff % dist == 0) {
            result--;
        }
        return result;
    }

    int addRungs(std::vector<int>& rungs, int dist) {
        int h = 0;
        int i = -1;
        int n = rungs.size();
        int result = 0;
        while (i < n - 1) {
            auto it = std::upper_bound(rungs.begin(), rungs.end(), h + dist);
            int ind = std::distance(rungs.begin(), it);

            if (ind - 1 > i) {
                i = ind - 1;
            } else {
                i = ind;
                result += insertRungs(rungs[i] - h, dist);
            }
            h = rungs[i];
        }
        int diff = rungs.back() - h;
        if (diff > 0) {
            result += insertRungs(diff, dist);
        }
        return result;
    }
};
// @lc code=end

