/*
 * @lc app=leetcode id=2050 lang=cpp
 *
 * [2050] Parallel Courses III
 */

// @lc code=start
#include <vector>
#include <queue>
#include <set>
using namespace std;

class Solution {
public:
    int minimumTime(int n, vector<vector<int>>& relations, vector<int>& time) {
        vector<set<int>> graph(n);
        vector<int> adj(n, 0);
        vector<int> dp(n, 0);
        queue<int> q;

        for (const vector<int>& rel : relations) {
            int prev = rel[0] - 1;
            int next = rel[1] - 1;
            graph[prev].insert(next);
            adj[next]++;
        }

        for (int i = 0; i < n; i++) {
            if (adj[i] == 0) {
                q.push(i);
            }
        }

        while (!q.empty()) {
            int course = q.front();
            q.pop();

            for (int next : graph[course]) {
                dp[next] = max(dp[next], dp[course] + time[course]);
                adj[next]--;
                if (adj[next] == 0) {
                    q.push(next);
                }
            }
        }

        int maxTime = 0;
        for (int i = 0; i < n; i++) {
            maxTime = max(maxTime, dp[i] + time[i]);
        }

        return maxTime;
    }
};

// @lc code=end

