/*
 * @lc app=leetcode id=1584 lang=cpp
 *
 * [1584] Min Cost to Connect All Points
 */

// @lc code=start
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

class UnionFindSet {
public:
    vector<int> parents;
    int count;

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

    void unionNodes(int u, int v) {
        int pu = find(u);
        int pv = find(v);
        if (pu != pv) {
            int pMax = max(pu, pv);
            int pMin = min(pu, pv);
            parents[pMax] = pMin;
            count--;
        }
    }
};

class Solution {
public:
    int minCostConnectPoints(vector<vector<int>>& points) {
        int n = points.size();
        priority_queue<vector<int>> pq;
        for (int i = 0; i < n - 1; ++i) {
            int xi = points[i][0];
            int yi = points[i][1];
            for (int j = i + 1; j < n; ++j) {
                int xj = points[j][0];
                int yj = points[j][1];
                int distance = abs(xi - xj) + abs(yi - yj);
                pq.push({-distance, i, j});
            }
        }

        UnionFindSet dsu(n);
        int result = 0;
        while (dsu.count > 1) {
            auto edge = pq.top();
            pq.pop();
            int distance = -edge[0];
            int u = edge[1];
            int v = edge[2];
            if (dsu.find(u) != dsu.find(v)) {
                dsu.unionNodes(u, v);
                result += distance;
            }
        }

        return result;
    }
};
// @lc code=end

