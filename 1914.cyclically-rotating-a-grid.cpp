/*
 * @lc app=leetcode id=1914 lang=cpp
 *
 * [1914] Cyclically Rotating a Grid
 */

// @lc code=start
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    vector<vector<int>> rotateGrid(vector<vector<int>>& grid, int k) {
        int m = grid.size();
        int n = grid[0].size();
        vector<vector<int>> result(m, vector<int>(n));
        vector<vector<bool>> visited(m, vector<bool>(n, false));
        
        vector<vector<vector<int>>> rings;
        
        for (int row = 0; row < m; row++) {
            if (row < n && !visited[row][row]) {
                vector<vector<int>> current;
                int i = row;
                int j = row;
                current.push_back({i, j});
                visited[i][j] = true;
                
                while (j + 1 < n && !visited[i][j + 1]) {
                    j++;
                    current.push_back({i, j});
                    visited[i][j] = true;
                }
                
                while (i + 1 < m && !visited[i + 1][j]) {
                    i++;
                    current.push_back({i, j});
                    visited[i][j] = true;
                }
                
                while (j - 1 >= 0 && !visited[i][j - 1]) {
                    j--;
                    current.push_back({i, j});
                    visited[i][j] = true;
                }
                
                while (i - 1 >= 0 && !visited[i - 1][j]) {
                    i--;
                    current.push_back({i, j});
                    visited[i][j] = true;
                }
                rings.push_back(current);
            }
        }
        
        for (int i = 0; i < rings.size(); i++) {
            for (int j = 0; j < rings[i].size(); j++) {
                vector<int> current = rings[i][j];
                vector<int> next = rings[i][(j + k) % rings[i].size()];
                result[current[0]][current[1]] = grid[next[0]][next[1]];
            }
        }
        
        return result;
    }
};

// @lc code=end

