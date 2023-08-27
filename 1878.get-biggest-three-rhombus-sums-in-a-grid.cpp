/*
 * @lc app=leetcode id=1878 lang=cpp
 *
 * [1878] Get Biggest Three Rhombus Sums in a Grid
 */

// @lc code=start
#include <vector>
#include <algorithm>
#include <unordered_set>

class Solution {
public:
    std::vector<int> getBiggestThree(std::vector<std::vector<int>>& grid) {
        int m = grid.size();
        int n = grid[0].size();
        std::unordered_set<int> result;
        
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                int maxSize = (m - 1 - i) / 2;
                int trueMaxSize = 0;
                int j1 = j, j2 = j;
                while (trueMaxSize <= maxSize && j1 < n && j2 >= 0) {
                    trueMaxSize++;
                    j1++;
                    j2--;
                }
                for (int k = 0; k < trueMaxSize; k++) {
                    int x = i, y = j;
                    int current = 0;
                    for (int l = 0; l < k; l++) {
                        x++;
                        y++;
                        current += grid[x][y];
                    }
                    for (int l = 0; l < k; l++) {
                        x++;
                        y--;
                        current += grid[x][y];
                    }
                    for (int l = 0; l < k; l++) {
                        x--;
                        y--;
                        current += grid[x][y];
                    }
                    for (int l = 0; l < k; l++) {
                        x--;
                        y++;
                        current += grid[x][y];
                    }
                    if (k > 0) {
                        result.insert(current);
                    } else {
                        result.insert(grid[x][y]);
                    }
                }
            }
        }
        
        std::vector<int> sortedResult(result.begin(), result.end());
        std::sort(sortedResult.rbegin(), sortedResult.rend());
        return {sortedResult.begin(), sortedResult.begin() + std::min(3, static_cast<int>(sortedResult.size()))};
    }
};
// @lc code=end

