/*
 * @lc app=leetcode id=542 lang=cpp
 *
 * [542] 01 Matrix
 */

// @lc code=start
#include <vector>
#include <queue>

class Solution {
public:
    std::vector<std::vector<int>> updateMatrix(std::vector<std::vector<int>>& mat) {
        int m = mat.size();
        int n = mat[0].size();
        int steps = 0;
        std::queue<std::pair<int, int>> queue;

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (mat[i][j] == 0) {
                    queue.push({i, j});
                }
            }
        }

        std::vector<std::vector<int>> result(m, std::vector<int>(n, 0));

        std::vector<std::vector<int>> directions = {
            {1, 0},
            {-1, 0},
            {0, 1},
            {0, -1}
        };

        while (!queue.empty()) {
            int count = queue.size();
            for (int i = 0; i < count; i++) {
                std::pair<int, int> coords = queue.front();
                queue.pop();
                int x = coords.first;
                int y = coords.second;
                result[x][y] = steps;

                for (const auto& direction : directions) {
                    int nx = x + direction[0];
                    int ny = y + direction[1];

                    if (nx >= 0 && nx < m && ny >= 0 && ny < n && mat[nx][ny] == 1) {
                        mat[nx][ny] = 0;
                        queue.push({nx, ny});
                    }
                }
            }
            steps++;
        }

        return result;
    }
};

// @lc code=end

