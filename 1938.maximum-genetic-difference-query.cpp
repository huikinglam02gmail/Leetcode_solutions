/*
 * @lc app=leetcode id=1938 lang=cpp
 *
 * [1938] Maximum Genetic Difference Query
 */

// @lc code=start
/*
 * @lc app=leetcode id=1938 lang=csharp
 *
 * [1938] Maximum Genetic Difference Query
 */

// @lc code=start
#include <vector>
#include <unordered_set>
#include <algorithm>

using std::max;
using std::unordered_set;
using std::vector;

class Solution {
private:
    vector<vector<vector<int>>> queryDict;
    vector<int> result;
    vector<unordered_set<int>> graph;
    int totalLevels;
    vector<vector<int>> prefixTree;

    void dfs(int node) {
        addNumToPrefixArray(node);
        for (vector<int>& query : queryDict[node]) 
        {
            result[query[0]] = getMaximumXOR(query[1]);
        }
        for (int child : graph[node]) {
            dfs(child);
        }
        removeNumToPrefixArray(node);
    }

    void addNumToPrefixArray(int num) {
        for (int i = totalLevels - 1; i >= 0; --i) {
            prefixTree[i][num >> i]++;
        }
    }

    void removeNumToPrefixArray(int num) {
        for (int i = totalLevels - 1; i >= 0; --i) {
            prefixTree[i][num >> i]--;
        }
    }

    int getMaximumXOR(int val) {
        int result = 0;
        for (int i = totalLevels - 1; i >= 0; --i) {
            int valBit = (val >> i) & 1;
            result <<= 1;
            result += (prefixTree[i][result + 1 - valBit] > 0) ? 1 - valBit : valBit;
        }
        return result ^ val;
    }

    int bitLength(int bits) {
        int size = 0;
        while (bits != 0) {
            bits >>= 1;
            size++;
        }
        return size;
    }    

public:
    vector<int> maxGeneticDifference(vector<int>& parents, vector<vector<int>>& queries) {
        int n = parents.size();
        graph.resize(n);
        queryDict.resize(n);
        result.resize(queries.size(), -1);
        auto maxVal = *max_element(queries.begin(), queries.end(), [](const vector<int> &a, const vector<int> &b){ return a[1] < b[1];});
        totalLevels = bitLength(max(n - 1, maxVal[1]));

        prefixTree.resize(totalLevels);
        for (int i = 0; i < totalLevels; ++i) {
            prefixTree[i].resize(1 << (totalLevels - i), 0);
        }

        int root = -1;
        for (int i = 0; i < n; ++i) {
            if (parents[i] != -1) {
                graph[parents[i]].insert(i);
            } else {
                root = i;
            }
        }

        for (int i = 0; i < queries.size(); i++) {
            queryDict[queries[i][0]].push_back({ i, queries[i][1] });
        }

        dfs(root);
        return result;
    }
};
// @lc code=end

// @lc code=end

