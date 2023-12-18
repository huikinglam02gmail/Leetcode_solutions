/*
 * @lc app=leetcode id=2017 lang=cpp
 *
 * [2017] Grid Game
 */

// @lc code=start
#include <vector>
#include <algorithm>
#include <numeric>

using namespace std;

class Solution {
public:
    /*
    First robot will proceed to the next row at some column. If it proceeds at index i, the second robot can get max(sum(grid[0][i + 1:]), sum(grid[:i]))
    */
    long long gridGame(vector<vector<int>>& grid) {
        long long result = LLONG_MAX;
        long long top = accumulate(grid[0].begin(), grid[0].end(), 0LL);
        long long bottom = 0;

        for (int i = 0; i < grid[0].size(); i++) {
            top -= grid[0][i];
            if (i > 0) bottom += grid[1][i - 1];
            result = min(result, max(top, bottom));
        }

        return result;
    }
};

// @lc code=end

