/*
 * @lc app=leetcode id=3033 lang=cpp
 *
 * [3033] Modify the Matrix
 */

// @lc code=start
#include <vector>
#include <algorithm>

using namespace std;

class Solution {
public:
    vector<vector<int>> modifiedMatrix(vector<vector<int>>& matrix) {
        int m = matrix.size();
        int n = matrix[0].size();
        for (int j = 0; j < n; j++) {
            int maxEle = -1;
            vector<int> negOnes;
            for (int i = 0; i < m; i++) {
                maxEle = max(maxEle, matrix[i][j]);
                if (matrix[i][j] == -1) negOnes.push_back(i);
            }
            for (int i : negOnes) matrix[i][j] = maxEle;
        }
        return matrix;
    }
};

// @lc code=end

