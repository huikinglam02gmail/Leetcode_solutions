/*
 * @lc app=leetcode id=815 lang=cpp
 *
 * [815] Bus Routes
 */

// @lc code=start
#include <vector>
#include <unordered_set>
#include <queue>

using namespace std;

class Solution {
public:
    int numBusesToDestination(vector<vector<int>>& routes, int source, int target) {
        if (source == target)
            return 0;

        int n = routes.size();
        vector<unordered_set<int>> stations(n);
        for (int i = 0; i < n; ++i) {
            stations[i] = unordered_set<int>(routes[i].begin(), routes[i].end());
        }

        vector<unordered_set<int>> graph(n);
        for (int i = 0; i < n; ++i) {
            graph[i] = unordered_set<int>();
        }

        for (int i = 0; i < n - 1; ++i) {
            for (int j = i + 1; j < n; ++j) {
                if (intersect(stations[i], stations[j])) {
                    graph[i].insert(j);
                    graph[j].insert(i);
                }
            }
        }

        queue<int> q;
        vector<bool> visited(n, false);
        int steps = 1;

        for (int i = 0; i < n; ++i) {
            if (stations[i].count(source) > 0) {
                visited[i] = true;
                q.push(i);
            }
        }

        while (!q.empty()) {
            int count = q.size();
            for (int i = 0; i < count; ++i) {
                int route = q.front();
                q.pop();

                if (stations[route].count(target) > 0) {
                    return steps;
                }

                for (int next : graph[route]) {
                    if (!visited[next]) {
                        visited[next] = true;
                        q.push(next);
                    }
                }
            }
            ++steps;
        }

        return -1;
    }

private:
    bool intersect(const unordered_set<int>& set1, const unordered_set<int>& set2) {
        for (int num : set1) {
            if (set2.count(num) > 0) {
                return true;
            }
        }
        return false;
    }
};

// @lc code=end

