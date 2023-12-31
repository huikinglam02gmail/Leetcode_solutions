/*
 * @lc app=leetcode id=2045 lang=cpp
 *
 * [2045] Second Minimum Time to Reach Destination
 */

// @lc code=start
#include <vector>
#include <queue>
#include <climits>
#include <unordered_set>

class Solution {
public:
    int secondMinimum(int n, std::vector<std::vector<int>>& edges, int time, int change) {
        std::vector<std::vector<int>> minimumTime(n, std::vector<int>{INT_MAX, INT_MAX});
        std::vector<std::unordered_set<int>> graph(n);

        for (const auto& edge : edges) {
            int u = edge[0] - 1;
            int v = edge[1] - 1;
            graph[u].insert(v);
            graph[v].insert(u);
        }

        minimumTime[0][0] = 0;
        std::queue<std::vector<int>> dq;
        dq.push({0, 0});

        while (!dq.empty()) {
            std::vector<int> current = dq.front();
            dq.pop();
            int node = current[0];
            int t = current[1];

            if ((t / change) % 2 == 1) {
                t = ((t / change) + 1) * change;
            }

            for (int nxt : graph[node]) {
                int nxtTime = t + time;

                if (minimumTime[nxt][0] > nxtTime) {
                    minimumTime[nxt][0] = nxtTime;
                    dq.push({nxt, nxtTime});
                } else if (minimumTime[nxt][0] < nxtTime && nxtTime < minimumTime[nxt][1]) {
                    minimumTime[nxt][1] = nxtTime;
                    dq.push({nxt, nxtTime});
                }
            }
        }

        return minimumTime[n - 1][1];
    }
};

// @lc code=end

