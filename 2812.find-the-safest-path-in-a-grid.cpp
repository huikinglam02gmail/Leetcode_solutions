/*
 * @lc app=leetcode id=2812 lang=cpp
 *
 * [2812] Find the Safest Path in a Grid
 */

// @lc code=start
#include <vector>
#include <queue>
#include <limits>

using namespace std;

class Solution {
private:
    vector<vector<int>> minD;
    int n;

public:
    bool CanReach(int thres) {
        queue<pair<int, int>> dq;
        vector<vector<bool>> visited(n, vector<bool>(n, false));

        if (minD[0][0] >= thres) {
            dq.push({0, 0});
            visited[0][0] = true;
        }

        while (!dq.empty()) {
            auto [x, y] = dq.front();
            dq.pop();

            if (x == n - 1 && y == n - 1) return true;

            vector<pair<int, int>> neigs = {{x - 1, y}, {x + 1, y}, {x, y - 1}, {x, y + 1}};

            for (auto [nx, ny] : neigs) {
                if (nx >= 0 && nx < n && ny >= 0 && ny < n && !visited[nx][ny] && minD[nx][ny] >= thres) {
                    visited[nx][ny] = true;
                    dq.push({nx, ny});
                }
            }
        }

        return false;
    }

    int maximumSafenessFactor(vector<vector<int>>& grid) {
        n = grid.size();
        minD = vector<vector<int>>(n, vector<int>(n, numeric_limits<int>::max()));

        queue<pair<int, int>> dq;

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 1) {
                    dq.push({i, j});
                    minD[i][j] = 0;
                }
            }
        }

        int steps = 1;
        while (!dq.empty()) {
            int count = dq.size();
            for (int k = 0; k < count; k++) {
                auto [x, y] = dq.front();
                dq.pop();

                vector<pair<int, int>> neigs = {{x - 1, y}, {x + 1, y}, {x, y - 1}, {x, y + 1}};

                for (auto [nx, ny] : neigs) {
                    if (nx >= 0 && nx < n && ny >= 0 && ny < n && minD[nx][ny] == numeric_limits<int>::max()) {
                        minD[nx][ny] = steps;
                        dq.push({nx, ny});
                    }
                }
            }
            steps++;
        }

        int l = 0, r = 2 * n - 1;
        while (l < r) {
            int mid = l + (r - l) / 2;
            bool canReach = CanReach(mid);
            if (canReach) {
                l = mid + 1;
            } else {
                r = mid;
            }
        }
        return l - 1;
    }
};

// @lc code=end

