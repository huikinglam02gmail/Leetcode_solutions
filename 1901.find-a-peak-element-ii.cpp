/*
 * @lc app=leetcode id=1901 lang=cpp
 *
 * [1901] Find a Peak Element II
 */

// @lc code=start
#include <vector>

class Solution {
public:
    std::vector<int> findPeakGrid(std::vector<std::vector<int>>& mat) {
        int m = mat.size();
        int n = mat[0].size();

        if (m > n) {
            std::vector<std::vector<int>> matTransposed = transpose(mat);
            std::vector<int> result = findPeakGrid(matTransposed);
            return { result[1], result[0] };
        } else if (n == 1) {
            return { 0, 0 };
        } else {
            int left = 0;
            int right = n;

            while (left < right) {
                int mid = left + (right - left) / 2;
                int row = getMaxRow(mat, mid);

                if ((mid == 0 || mat[row][mid - 1] < mat[row][mid]) &&
                    (mid == n - 1 || mat[row][mid + 1] < mat[row][mid])) {
                    return { row, mid };
                } else if (mid > 0 && mat[row][mid - 1] > mat[row][mid]) {
                    right = mid;
                } else {
                    left = mid + 1;
                }
            }

            return { getMaxRow(mat, left), left };
        }
    }

private:
    std::vector<std::vector<int>> transpose(std::vector<std::vector<int>>& mat) {
        int m = mat.size();
        int n = mat[0].size();
        std::vector<std::vector<int>> result(n, std::vector<int>(m));

        for (int j = 0; j < n; j++) {
            for (int i = 0; i < m; i++) {
                result[j][i] = mat[i][j];
            }
        }

        return result;
    }

    int getMaxRow(std::vector<std::vector<int>>& mat, int col) {
        int row = 0;
        int current = -1;

        for (int i = 0; i < mat.size(); i++) {
            if (mat[i][col] > current) {
                current = mat[i][col];
                row = i;
            }
        }

        return row;
    }
};

// @lc code=end

