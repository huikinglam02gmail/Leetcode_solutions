/*
 * @lc app=leetcode id=1337 lang=cpp
 *
 * [1337] The K Weakest Rows in a Matrix
 */

// @lc code=start
#include <vector>
#include <algorithm>

using std::accumulate;

class Solution {
public:
    std::vector<int> kWeakestRows(std::vector<std::vector<int>>& mat, int k) {
        std::vector<std::pair<int, int>> sumIndices;
        int m = mat.size();
        
        for (int i = 0; i < m; ++i) {
            int rowSum = accumulate(mat[i].begin(), mat[i].end(), 0);
            sumIndices.emplace_back(rowSum, i);
        }
        
        std::sort(sumIndices.begin(), sumIndices.end());
        
        std::vector<int> result;
        for (int i = 0; i < k; ++i) {
            result.emplace_back(sumIndices[i].second);
        }
        
        return result;
    }
};

// @lc code=end

