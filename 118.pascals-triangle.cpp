/*
 * @lc app=leetcode id=118 lang=cpp
 *
 * [118] Pascal's Triangle
 */

// @lc code=start
class Solution {
public:
    vector<vector<int>> generate(int numRows) {
        vector<vector<int>> triangle;

        for (int i = 0; i < numRows; i++) {
            vector<int> row;

            for (int j = 0; j <= i; j++) {
                if (j == 0 || j == i) {
                    row.push_back(1);
                } else {
                    row.push_back(triangle[i - 1][j - 1] + triangle[i - 1][j]);
                }
            }

            triangle.push_back(row);
        }

        return triangle;
    }
};

// @lc code=end

