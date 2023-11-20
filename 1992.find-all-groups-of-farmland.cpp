/*
 * @lc app=leetcode id=1992 lang=cpp
 *
 * [1992] Find All Groups of Farmland
 */

// @lc code=start
#include <vector>
#include <queue>

class Solution {
public:
    std::vector<std::vector<int>> findFarmland(std::vector<std::vector<int>>& land) {
        int m = land.size();
        int n = land[0].size();
        std::vector<std::vector<int>> result;
        std::vector<std::vector<bool>> visited(m, std::vector<bool>(n, false));
        for (int i = 0; i < m; ++i)
        {
            for (int j = 0; j < n; ++j)
            {
                visited[i][j] = (land[i][j] == 0);
            }
        }

        for (int i = 0; i < m; i++)
        {
            for (int j = 0; j < n; j++)
            {
                if (!visited[i][j])
                {
                    std::queue<std::vector<int>> queue;
                    queue.push({i, j, i, j});
                    visited[i][j] = true;

                    while (!queue.empty())
                    {
                        std::vector<int> coordinates = queue.front();
                        queue.pop();
                        int x1 = coordinates[0], y1 = coordinates[1], x2 = coordinates[2], y2 = coordinates[3];

                        if ((x2 == m - 1 || land[x2 + 1][y2] == 0) && (y2 == n - 1 || land[x2][y2 + 1] == 0))
                        {
                            result.push_back({x1, y1, x2, y2});
                        }
                        else
                        {
                            if (x2 + 1 < m && !visited[x2 + 1][y2])
                            {
                                visited[x2 + 1][y2] = true;
                                queue.push({x1, y1, x2 + 1, y2});
                            }
                            if (y2 + 1 < n && !visited[x2][y2 + 1])
                            {
                                visited[x2][y2 + 1] = true;
                                queue.push({x1, y1, x2, y2 + 1});
                            }
                        }
                    }
                }
            }
        }

        return result;
    }
};

// @lc code=end

