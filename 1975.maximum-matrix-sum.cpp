/*
 * @lc app=leetcode id=1975 lang=cpp
 *
 * [1975] Maximum Matrix Sum
 */

// @lc code=start
#include <vector>
#include <algorithm>

class Solution {
public:
    long long maxMatrixSum(std::vector<std::vector<int>>& matrix) {
        int m = matrix.size();
        int n = matrix[0].size();
        int zeros = 0, negs = 0;
        long long S = 0, minAbsSoFar = LLONG_MAX;

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                S += std::abs(matrix[i][j]);
                if (matrix[i][j] == 0) {
                    zeros++;
                }
                else if (matrix[i][j] < 0) {
                    negs++;
                }
                minAbsSoFar = std::min(minAbsSoFar, static_cast<long long>(std::abs(matrix[i][j])));
            }
        }

        return zeros > 0 || negs % 2 == 0 ? S : S - 2 * minAbsSoFar;
    }
};

// @lc code=end

