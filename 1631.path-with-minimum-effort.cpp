/*
 * @lc app=leetcode id=1631 lang=cpp
 *
 * [1631] Path With Minimum Effort
 */

// @lc code=start
#include <vector>
#include <queue>
#include <climits>

using namespace std;

class Solution {
public:
    int minimumEffortPath(vector<vector<int>>& heights) {
        int m = heights.size();
        int n = heights[0].size();
        vector<vector<int>> effort(m, vector<int>(n, INT_MAX));
        priority_queue<vector<int>, vector<vector<int>>, greater<vector<int>>> pq;

        pq.push({0, 0, 0});  // {effort, x, y}

        vector<vector<int>> directions = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};

        while (!pq.empty()) {
            vector<int> top = pq.top();
            pq.pop();
            int curEffort = top[0];
            int x = top[1];
            int y = top[2];

            if (x == m - 1 && y == n - 1) {
                return curEffort;
            }

            if (curEffort > effort[x][y]) {
                continue;
            }

            for (const vector<int>& dir : directions) {
                int newX = x + dir[0];
                int newY = y + dir[1];

                if (newX >= 0 && newX < m && newY >= 0 && newY < n) {
                    int newEffort = max(curEffort, abs(heights[newX][newY] - heights[x][y]));
                    if (newEffort < effort[newX][newY]) {
                        effort[newX][newY] = newEffort;
                        pq.push({newEffort, newX, newY});
                    }
                }
            }
        }

        return -1;  // Should not reach here
    }
};
// @lc code=end

