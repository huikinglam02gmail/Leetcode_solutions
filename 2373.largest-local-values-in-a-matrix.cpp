/*
 * @lc app=leetcode id=2373 lang=cpp
 *
 * [2373] Largest Local Values in a Matrix
 */

// @lc code=start
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    vector<vector<int>> largestLocal(vector<vector<int>>& grid) {
        vector<vector<int>> result;
        int n = grid.size();
        for (int i = 1; i < n - 1; i++) {
            vector<int> row;
            for (int j = 1; j < n - 1; j++) {
                row.push_back(max(max(max(max(max(max(max(grid[i - 1][j - 1], grid[i - 1][j]), grid[i - 1][j + 1]), grid[i][j - 1]), grid[i][j]), grid[i][j + 1]), grid[i + 1][j - 1]), max(grid[i + 1][j], grid[i + 1][j + 1])));
            }
            result.push_back(row);
        }
        return result;
    }
};

// @lc code=end

