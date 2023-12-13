/*
 * @lc app=leetcode id=1582 lang=cpp
 *
 * [1582] Special Positions in a Binary Matrix
 */

// @lc code=start
#include <vector>

class Solution {
public:
    int numSpecial(std::vector<std::vector<int>>& mat) {
        int result = 0;
        std::vector<int> rowSum(mat.size(), 0);
        std::vector<int> columnSum(mat[0].size(), 0);

        for (int i = 0; i < mat.size(); i++) {
            for (int j = 0; j < mat[0].size(); j++) {
                rowSum[i] += mat[i][j];
                columnSum[j] += mat[i][j];
            }
        }

        for (int i = 0; i < mat.size(); i++) {
            for (int j = 0; j < mat[0].size(); j++) {
                if (mat[i][j] == 1 && rowSum[i] == 1 && columnSum[j] == 1) {
                    result++;
                }
            }
        }

        return result;
    }
};

// @lc code=end

