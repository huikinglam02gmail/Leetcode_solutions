/*
 * @lc app=leetcode id=802 lang=cpp
 *
 * [802] Find Eventual Safe States
 */

// @lc code=start
#include <vector>
#include <queue>
#include <unordered_set>
#include <algorithm>
using std::queue;
using std::sort;
using std::unordered_set;
using std::vector;

class Solution {
public:
    vector<int> eventualSafeNodes(vector<vector<int>>& graph) {
        int n = graph.size();
        vector<int> degree(n);
        vector<vector<int>> source(n);

        for (int i = 0; i < n; i++) {
            degree[i] = graph[i].size();
            for (int item : graph[i]) {
                source[item].push_back(i);
            }
        }

        unordered_set<int> safe {};
        queue<int> queue {};

        for (int i = 0; i < n; i++) {
            if (degree[i] == 0) {
                safe.insert(i);
                queue.push(i);
            }
        }

        while (!queue.empty()) {
            int node = queue.front();
            queue.pop();

            for (int item : source[node]) {
                degree[item]--;
                if (degree[item] == 0) {
                    safe.insert(item);
                    queue.push(item);
                }
            }
        }

        vector<int> result(safe.begin(), safe.end());
        sort(result.begin(), result.end());

        return result;
    }
};

// @lc code=end

