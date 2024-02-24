/*
 * @lc app=leetcode id=2092 lang=cpp
 *
 * [2092] Find All People With Secret
 */

// @lc code=start
#include <vector>
#include <algorithm>
#include <unordered_map>
#include <queue>
#include <unordered_set>

class UnionFindSet {
private:
    std::vector<int> parents;
    int count;

public:
    UnionFindSet(int n) : parents(n), count(n) {
        for (int i = 0; i < n; ++i) {
            parents[i] = i;
        }
    }

    int find(int u) {
        if (u != parents[u]) {
            parents[u] = find(parents[u]);
        }
        return parents[u];
    }

    void unionSet(int u, int v) {
        int pu = find(u);
        int pv = find(v);
        if (pu != pv) {
            int pMax = std::max(pu, pv);
            int pMin = std::min(pu, pv);
            parents[pMax] = pMin;
            --count;
        }
    }

    int getCount() const {
        return count;
    }
};

class Solution {
public:
    std::vector<int> findAllPeople(int n, std::vector<std::vector<int>>& meetings, int firstPerson) {
        meetings.insert(meetings.begin(), {0, firstPerson, 0});
        std::sort(meetings.begin(), meetings.end(), [](const auto& a, const auto& b) {
            return a[2] < b[2];
        });

        UnionFindSet uf(n + 1);
        int i = 0, t = 0;
        while (i < meetings.size()) {
            t = meetings[i][2];
            std::unordered_map<int, std::unordered_set<int>> graph;
            std::queue<int> dq;
            std::unordered_set<int> visited;
            while (i < meetings.size() && t == meetings[i][2]) {
                int u = meetings[i][0];
                int v = meetings[i][1];
                if (graph.find(u) == graph.end()) {
                    graph[u] = {};
                }
                if (graph.find(v) == graph.end()) {
                    graph[v] = {};
                }
                graph[u].insert(v);
                graph[v].insert(u);
                if (uf.find(u) == 0 && visited.find(u) == visited.end()) {
                    dq.push(u);
                    visited.insert(u);
                }
                if (uf.find(v) == 0 && visited.find(v) == visited.end()) {
                    dq.push(v);
                    visited.insert(v);
                }
                ++i;
            }
            while (!dq.empty()) {
                int node = dq.front();
                dq.pop();
                for (int nxt : graph[node]) {
                    if (visited.find(nxt) == visited.end()) {
                        if (uf.find(nxt) > 0) {
                            uf.unionSet(0, nxt);
                        }
                        dq.push(nxt);
                        visited.insert(nxt);
                    }
                }
            }
        }
        std::vector<int> result;
        for (int i = 0; i <= n; ++i) {
            if (uf.find(i) == 0) {
                result.push_back(i);
            }
        }
        return result;
    }
};

// @lc code=end

