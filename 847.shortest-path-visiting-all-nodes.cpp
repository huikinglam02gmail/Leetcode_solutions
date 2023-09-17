/*
 * @lc app=leetcode id=847 lang=cpp
 *
 * [847] Shortest Path Visiting All Nodes
 */

// @lc code=start
#include <iostream>
#include <vector>
#include <queue>
#include <unordered_set>

class Solution {
public:
    int shortestPathLength(std::vector<std::vector<int>>& graph) {
        int n = graph.size();
        std::queue<std::pair<int, int>> q;
        std::unordered_set<std::pair<int, int>, PairHash> visited;
        int steps = 0;

        for (int i = 0; i < n; i++) {
            q.push({i, 1 << i});
            visited.insert({i, 1 << i});
        }

        while (!q.empty()) {
            int qSize = q.size();

            for (int i = 0; i < qSize; i++) {
                auto [node, mask] = q.front();
                q.pop();

                if (mask == (1 << n) - 1) {
                    return steps;
                }

                for (int neighbor : graph[node]) {
                    int newMask = mask | (1 << neighbor);

                    if (visited.find({neighbor, newMask}) == visited.end()) {
                        q.push({neighbor, newMask});
                        visited.insert({neighbor, newMask});
                    }
                }
            }

            steps++;
        }

        return -1; // Should not reach here
    }

private:
    struct PairHash {
        template <class T1, class T2>
        std::size_t operator () (const std::pair<T1, T2>& p) const {
            auto h1 = std::hash<T1>{}(p.first);
            auto h2 = std::hash<T2>{}(p.second);
            return h1 ^ h2;
        }
    };
};

// @lc code=end

