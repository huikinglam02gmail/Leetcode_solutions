/*
 * @lc app=leetcode id=1971 lang=cpp
 *
 * [1971] Find if Path Exists in Graph
 */

// @lc code=start
#include <vector>
#include <unordered_set>
#include <deque>

using namespace std;

class Solution {
public:
    bool validPath(int n, vector<vector<int>>& edges, int source, int destination) {
        vector<unordered_set<int>> graph(n);
        for (const auto& edge : edges) {
            graph[edge[0]].insert(edge[1]);
            graph[edge[1]].insert(edge[0]);
        }

        deque<int> dq;
        unordered_set<int> visited;
        dq.push_back(source);
        visited.insert(source);
        while (!dq.empty()) {
            int node = dq.front();
            dq.pop_front();
            if (node == destination) {
                return true;
            }
            for (int nxt : graph[node]) {
                if (visited.find(nxt) == visited.end()) {
                    visited.insert(nxt);
                    dq.push_back(nxt);
                }
            }
        }
        return false;
    }
};

// @lc code=end

