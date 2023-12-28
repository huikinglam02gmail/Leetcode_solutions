/*
 * @lc app=leetcode id=2039 lang=cpp
 *
 * [2039] The Time When the Network Becomes Idle
 */

// @lc code=start
#include <iostream>
#include <vector>
#include <unordered_set>
#include <queue>
#include <algorithm>

class Solution {
public:
    int networkBecomesIdle(std::vector<std::vector<int>>& edges, std::vector<int>& patience) {
        int n = patience.size();
        std::vector<int> dist(n, -1);
        std::vector<bool> visited(n, false);
        std::vector<std::unordered_set<int>> graph(n);

        for (const auto& edge : edges) {
            int u = edge[0];
            int v = edge[1];
            graph[u].insert(v);
            graph[v].insert(u);
        }

        std::queue<int> dq;
        dq.push(0);
        visited[0] = true;
        int steps = 0;

        while (!dq.empty()) {
            int count = dq.size();
            for (int i = 0; i < count; i++) {
                int node = dq.front();
                dq.pop();
                dist[node] = steps;
                for (int nxt : graph[node]) {
                    if (!visited[nxt]) {
                        dq.push(nxt);
                        visited[nxt] = true;
                    }
                }
            }
            steps += 2;
        }

        int result = 0;
        for (int i = 1; i < n; i++) {
            int lastOut = ((dist[i] - 1) / patience[i]) * patience[i];
            result = std::max(result, dist[i] + 1 + lastOut);
        }

        return result;
    }
};

// @lc code=end

