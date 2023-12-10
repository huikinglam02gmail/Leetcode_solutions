/*
 * @lc app=leetcode id=867 lang=cpp
 *
 * [867] Transpose Matrix
 */

// @lc code=start
#include <vector>

using namespace std;

class Solution {
public:
    vector<vector<int>> transpose(vector<vector<int>>& matrix) {
        int m = matrix.size();
        int n = matrix[0].size();

        vector<vector<int>> transposed(n, vector<int>(m, 0));

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                transposed[i][j] = matrix[j][i];
            }
        }

        return transposed;
    }
};

// @lc code=end

