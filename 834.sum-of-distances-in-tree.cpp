/*
 * @lc app=leetcode id=834 lang=cpp
 *
 * [834] Sum of Distances in Tree
 */

// @lc code=start
#include <vector>
#include <unordered_set>

using namespace std;

class Solution {
private:
    vector<int> weight;
    vector<int> answer;
    vector<unordered_set<int>> graph;

public:
    vector<int> dfs(int node, int parent, int depth) {
        int count = 1, distance = depth;
        for (int child : graph[node]) {
            if (child != parent) {
                vector<int> child_data = dfs(child, node, depth + 1);
                count += child_data[0];
                distance += child_data[1];
            }
        }
        weight[node] = count;
        return {count, distance};
    }

    void dfs2(int node, int parent, int n) {
        for (int child : graph[node]) {
            if (child != parent) {
                answer[child] = answer[node] + n - 2 * weight[child];
                dfs2(child, node, n);
            }
        }
    }

    vector<int> sumOfDistancesInTree(int n, vector<vector<int>>& edges) {
        graph.resize(n);
        for (auto& edge : edges) {
            graph[edge[0]].insert(edge[1]);
            graph[edge[1]].insert(edge[0]);
        }
        weight.resize(n);
        answer.resize(n);
        int root = 0;
        vector<int> root_data = dfs(root, -1, 0);
        int count = root_data[0];
        answer[root] = root_data[1];
        dfs2(root, -1, n);
        return answer;
    }
};

// @lc code=end

