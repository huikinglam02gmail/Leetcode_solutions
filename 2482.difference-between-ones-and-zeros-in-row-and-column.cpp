/*
 * @lc app=leetcode id=2482 lang=cpp
 *
 * [2482] Difference Between Ones and Zeros in Row and Column
 */

// @lc code=start
#include <iostream>
#include <vector>

class Solution {
public:
    /*
    onesRow[i] = n - zerosRow[i]
    onesCol[j] = m - zerosCol[j]
    diff[i][j] = n - 2 * zerosRow[i] + m - 2 * zerosCol[j]
    */
    std::vector<std::vector<int>> onesMinusZeros(std::vector<std::vector<int>>& grid) {
        int m = grid.size();
        int n = grid[0].size();
        std::vector<int> zerosRow(m, 0);
        std::vector<int> zerosCol(n, 0);
        std::vector<std::vector<int>> diff(m, std::vector<int>(n, 0));

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 0) {
                    zerosRow[i]++;
                    zerosCol[j]++;
                }
            }
        }

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                diff[i][j] = m + n - 2 * (zerosRow[i] + zerosCol[j]);
            }
        }

        return diff;
    }
};

// @lc code=end

