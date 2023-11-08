/*
 * @lc app=leetcode id=2849 lang=cpp
 *
 * [2849] Determine if a Cell Is Reachable at a Given Time
 */

// @lc code=start
#include <algorithm>
using std::abs;
using std::max;
class Solution {
public:
    bool isReachableAtTime(int sx, int sy, int fx, int fy, int t) {
        int need = max(abs(sx - fx), abs(sy - fy));
        if (need == 0 && t == 1) return false;
        return need <= t;
    }
};

// @lc code=end

