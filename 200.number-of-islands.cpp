/*
 * @lc app=leetcode id=200 lang=cpp
 *
 * [200] Number of Islands
 */

// @lc code=start
#include <vector>
#include <deque>

using namespace std;

class Solution {
public:
    int numIslands(vector<vector<char>>& grid) {
        int m = grid.size();
        int n = grid[0].size();
        int result = 0;

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == '1') {
                    deque<pair<int, int>> dq;
                    dq.push_back({i, j});
                    grid[i][j] = '0';
                    while (!dq.empty()) {
                        auto node = dq.front();
                        dq.pop_front();
                        vector<vector<int>> neigs = {{0, 1}, {1, 0}, {-1, 0}, {0, -1}};
                        for (const auto& neig : neigs) {
                            int new_i = node.first + neig[0];
                            int new_j = node.second + neig[1];
                            if (new_i >= 0 && new_i < m && new_j >= 0 && new_j < n && grid[new_i][new_j] == '1') {
                                dq.push_back({new_i, new_j});
                                grid[new_i][new_j] = '0';
                            }
                        }
                    }
                    result++;
                }
            }
        }
        return result;
    }
};

// @lc code=end

