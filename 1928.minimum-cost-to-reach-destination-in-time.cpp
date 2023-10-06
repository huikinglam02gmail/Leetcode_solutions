/*
 * @lc app=leetcode id=1928 lang=cpp
 *
 * [1928] Minimum Cost to Reach Destination in Time
 */

// @lc code=start
#include <vector>
#include <queue>
#include <unordered_map>
#include <climits>

class Solution {
public:
    int minCost(int maxTime, std::vector<std::vector<int>>& edges, std::vector<int>& passingFees) {
        int n = passingFees.size();
        std::vector<std::vector<std::pair<int, int>>> graph(n);
        
        for (const auto& edge : edges) {
            int x = edge[0];
            int y = edge[1];
            int time = edge[2];
            graph[x].emplace_back(y, time);
            graph[y].emplace_back(x, time);
        }
        
        std::priority_queue<std::vector<int>, std::vector<std::vector<int>>, std::greater<std::vector<int>>> pq;
        std::vector<int> arrivals(n, INT_MAX);
        pq.push({passingFees[0], 0, 0});
        
        while (!pq.empty()) {
            std::vector<int> info = pq.top();
            pq.pop();
            int cost = info[0];
            int node = info[1];
            int time = info[2];
            
            if (time > maxTime) {
                continue;
            }
            
            if (node == n - 1) {
                return cost;
            }
            
            if (time < arrivals[node]) {
                arrivals[node] = time;
                for (const auto& neighbor : graph[node]) {
                    int neighborNode = neighbor.first;
                    int neighborTime = time + neighbor.second;
                    pq.push({passingFees[neighborNode] + cost, neighborNode, neighborTime});
                }
            }
        }
        
        return -1;
    }
};

// @lc code=end

