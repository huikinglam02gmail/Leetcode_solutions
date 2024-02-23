/*
 * @lc app=leetcode id=787 lang=cpp
 *
 * [787] Cheapest Flights Within K Stops
 */

// @lc code=start
#include <vector>
#include <unordered_map>
#include <queue>
#include <limits>

class Solution {
public:
    int findCheapestPrice(int n, std::vector<std::vector<int>>& flights, int src, int dst, int k) {
        std::vector<std::unordered_map<int, int>> graph(n);
        for (const auto& flight : flights) {
            graph[flight[0]][flight[1]] = flight[2];
        }
        std::vector<int> visited(n, std::numeric_limits<int>::max());
        std::priority_queue<std::vector<int>, std::vector<std::vector<int>>, std::greater<std::vector<int>>> pq;
        pq.push({0, src, 0});
        while (!pq.empty()) {
            auto node = pq.top();
            pq.pop();
            int cost = node[0];
            int city = node[1];
            int stops = node[2];
            if (city == dst) {
                return cost;
            }
            if (stops < k + 1) {
                visited[city] = stops;
                for (const auto& neighbor : graph[city]) {
                    int neighborCity = neighbor.first;
                    int neighborCost = neighbor.second;
                    if (stops + 1 < visited[neighborCity]) {
                        pq.push({cost + neighborCost, neighborCity, stops + 1});
                    }
                }
            }
        }
        return -1;
    }
};

// @lc code=end

