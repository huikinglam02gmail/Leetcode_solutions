/*
 * @lc app=leetcode id=1219 lang=cpp
 *
 * [1219] Path with Maximum Gold
 */

// @lc code=start
#include <vector>
#include <algorithm>

class Solution {
private:
    std::vector<std::vector<int>> grid;

    int dfs(int x, int y) {
        if (x < 0 || y < 0 || x >= grid.size() || y >= grid[0].size() || grid[x][y] == 0) return 0;
        int original = grid[x][y];
        int result = 0;
        std::vector<std::vector<int>> neigs = {{x - 1, y}, {x + 1, y}, {x, y - 1}, {x, y + 1}};
        grid[x][y] = 0;
        for (const auto& nei : neigs) {
            result = std::max(result, dfs(nei[0], nei[1]));
        }
        grid[x][y] = original;
        return result + original;
    }

public:
    int getMaximumGold(std::vector<std::vector<int>>& grid) {
        int m = grid.size();
        int n = grid[0].size();
        int total = 0;
        for (const auto& row : grid) {
            for (int cell : row) {
                total += cell;
            }
        }
        this->grid = grid;
        int result = 0;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                result = std::max(result, dfs(i, j));
                if (result == total) return total;
            }
        }
        return result;
    }
};

// @lc code=end

