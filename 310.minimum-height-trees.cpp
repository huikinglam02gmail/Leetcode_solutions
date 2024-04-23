/*
 * @lc app=leetcode id=310 lang=cpp
 *
 * [310] Minimum Height Trees
 */

// @lc code=start
#include <vector>
#include <unordered_set>

using namespace std;

class Solution {
public:
    /*
    There can only be up to two possible roots. Just bfs from leaves until only <= 2 nodes remaining
    */
    vector<int> findMinHeightTrees(int n, vector<vector<int>>& edges) {
        if (edges.size() == 0) {
            return {0};
        } else if (edges.size() == 1) {
            return {0, 1};
        } else {
            vector<unordered_set<int>> neighbors(n);
            for (const auto& edge : edges) {
                neighbors[edge[0]].insert(edge[1]);
                neighbors[edge[1]].insert(edge[0]);
            }
            vector<int> leaves;
            for (int i = 0; i < n; i++) {
                if (neighbors[i].size() == 1) leaves.push_back(i);
            }
            int remaining = n;
            while (remaining > 2) {
                vector<int> newLeaves;
                while (!leaves.empty()) {
                    int leaf = leaves.back();
                    leaves.pop_back();
                    int neighbor = *(neighbors[leaf].begin()); // simply connected, only 1 neighbour left
                    remaining--;
                    neighbors[neighbor].erase(leaf);
                    if (neighbors[neighbor].size() == 1) newLeaves.push_back(neighbor);
                }
                leaves = newLeaves;
            }
            return leaves;
        }
    }
};

// @lc code=end

