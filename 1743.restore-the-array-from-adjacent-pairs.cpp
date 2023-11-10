/*
 * @lc app=leetcode id=1743 lang=cpp
 *
 * [1743] Restore the Array From Adjacent Pairs
 */

// @lc code=start
#include <vector>
#include <unordered_map>
#include <unordered_set>
#include <queue>

class Solution {
public:
    std::vector<int> restoreArray(std::vector<std::vector<int>>& adjacentPairs) {
        std::unordered_map<int, std::unordered_set<int>> graph;
        
        for (const auto& pair : adjacentPairs) {
            int a = pair[0];
            int b = pair[1];
            
            if (graph.find(a) == graph.end()) {
                graph[a] = std::unordered_set<int>();
            }
            if (graph.find(b) == graph.end()) {
                graph[b] = std::unordered_set<int>();
            }
            
            graph[a].insert(b);
            graph[b].insert(a);
        }
        
        int start;
        for (const auto& entry : graph) {
            if (entry.second.size() == 1) {
                start = entry.first;
                break;
            }
        }
        
        std::deque<int> dq;
        std::unordered_set<int> visited;
        
        dq.push_back(start);
        visited.insert(start);
        
        std::vector<int> result;
        
        while (!dq.empty()) {
            result.push_back(dq.front());
            dq.pop_front();
            
            for (int nxt : graph[result.back()]) {
                if (visited.find(nxt) == visited.end()) {
                    dq.push_back(nxt);
                    visited.insert(nxt);
                }
            }
        }
        
        return result;
    }
};

// @lc code=end

