/*
 * @lc app=leetcode id=1981 lang=cpp
 *
 * [1981] Minimize the Difference Between Target and Chosen Elements
 */

// @lc code=start
/*
 * @lc app=leetcode id=1981 lang=cpp
 *
 * [1981] Minimize the Difference Between Target and Chosen Elements
 */

// @lc code=start
#include <vector>
#include <unordered_set>

class Solution {
public:
    int minimizeTheDifference(vector<vector<int>>& mat, int target) {
    bool bt[70 * 70 + 1] = {};
    int max_e = 0, res = INT_MAX;
    bt[0] = true;
    for (auto & row : mat) {
        bool bt1[70 * 70 + 1] = {};
        int max_e1 = 0;
        for (auto i : unordered_set(begin(row), end(row))) {
            for (int j = 0; j <= max_e; ++j)
                if (bt[j]) {
                    bt1[i + j] = true;
                    max_e1 = max(max_e1, i + j);
                }
        }
        swap(bt, bt1);
        max_e = max_e1;
    }
    for (int i = 0; i <= 70 * 70; ++i) {
        if (bt[i]) res = min(res, abs(i - target));
    }
    return res;
}
};

// @lc code=end



// @lc code=end

