/*
 * @lc app=leetcode id=1489 lang=cpp
 *
 * [1489] Find Critical and Pseudo-Critical Edges in Minimum Spanning Tree
 */

// @lc code=start
#include <vector>
#include <algorithm>
#include <unordered_map>
#include <unordered_set>
using std::copy;
using std::sort;
using std::unordered_map;
using std::vector;

class UnionFindSet {
public:
    std::vector<int> parents;
    int count;

    UnionFindSet(int n = 0) {
        parents.resize(n);
        for (int i = 0; i < n; i++)
        {
            parents[i] = i;
        }
        count = n;
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
            count--;
        }
    }
};

class Solution {
public:
    vector<vector<int>> findCriticalAndPseudoCriticalEdges(int n, vector<vector<int>>& edges) {
        vector<int> critical;
        vector<int> pseudo;
        UnionFindSet DS(n);
        vector<int> oldParents(n);
        int oldCount = n;

        unordered_map<int, vector<vector<int>>> weights;
        for (int i = 0; i < edges.size(); i++)
        {
            if (weights.find(edges[i][2]) == weights.end())
            {
                weights.insert({edges[i][2], vector<vector<int>> {}});
            }
            weights[edges[i][2]].push_back(vector<int>{edges[i][0], edges[i][1], i});
        }

        vector<int> sortedWeights;
        for (const auto& entry : weights) {
            sortedWeights.push_back(entry.first);
        }
        sort(sortedWeights.begin(), sortedWeights.end());

        for (int w : sortedWeights) {
            vector<vector<int>> nonRedundant;
            for (const auto& item : weights[w]) {
                if (DS.find(item[0]) != DS.find(item[1])) {
                    nonRedundant.push_back(item);
                }
            }
            copy(DS.parents.begin(), DS.parents.end(), oldParents.begin());
            oldCount = DS.count;
            
            for (int j = 0; j < nonRedundant.size(); j++) {
                for (int k = 0; k < nonRedundant.size(); k++) {
                    if (k != j) {
                        DS.unionSet(nonRedundant[k][0], nonRedundant[k][1]);
                    }
                }
                int countPrev = DS.count;
                DS.unionSet(nonRedundant[j][0], nonRedundant[j][1]);
                if (DS.count < countPrev) {
                    critical.push_back(nonRedundant[j][2]);
                } else {
                    pseudo.push_back(nonRedundant[j][2]);
                }
                copy(oldParents.begin(), oldParents.end(), DS.parents.begin());
                DS.count = oldCount;
            }

            for (const auto& item : nonRedundant) {
                DS.unionSet(item[0], item[1]);
            }
        }

        return {critical, pseudo};
    }
};
// @lc code=end

