/*
 * @lc app=leetcode id=463 lang=cpp
 *
 * [463] Island Perimeter
 */

// @lc code=start
#include <vector>

using namespace std;

class Solution {
public:
    int islandPerimeter(vector<vector<int>>& grid) {
        int width = grid.size();
        int height = grid[0].size();
        int touching = 0;
        int count = 0;
        for (int i = 0; i < width; i++) {
            for (int j = 0; j < height; j++) {
                if (grid[i][j] == 1) {
                    count++;
                }
                if (i != width - 1 && grid[i][j] == 1 && grid[i + 1][j] == 1) {
                    touching++;
                }
                if (j != height - 1 && grid[i][j] == 1 && grid[i][j + 1] == 1) {
                    touching++;
                }
            }
        }
        return count * 4 - 2 * touching;
    }
};

// @lc code=end

