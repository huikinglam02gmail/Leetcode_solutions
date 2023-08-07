/*
 * @lc app=leetcode id=74 lang=cpp
 *
 * [74] Search a 2D Matrix
 */

// @lc code=start
#include <vector>

class Solution {
public:
    bool searchMatrix(std::vector<std::vector<int>>& matrix, int target) {
        int row = 0;
        int col = matrix[0].size() - 1;

        while (row >= 0 && row < matrix.size() && col >= 0 && col < matrix[0].size()) {
            if (matrix[row][col] < target) {
                row++;
            } else if (matrix[row][col] > target) {
                col--;
            } else {
                return true;
            }
        }

        return false;
    }
};

// @lc code=end

