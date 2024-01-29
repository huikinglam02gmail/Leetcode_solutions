/*
 * @lc app=leetcode id=2639 lang=cpp
 *
 * [2639] Find the Width of Columns of a Grid
 */

// @lc code=start
#include <vector>
#include <algorithm>

class Solution {
public:
    std::vector<int> findColumnWidth(std::vector<std::vector<int>>& grid) {
        int m = grid.size();
        int n = grid[0].size();
        std::vector<int> result(n, 0);

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                result[j] = std::max(result[j], static_cast<int>(std::to_string(grid[i][j]).length()));
            }
        }

        return result;
    }
};

// @lc code=end

