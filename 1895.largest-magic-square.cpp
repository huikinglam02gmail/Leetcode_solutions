/*
 * @lc app=leetcode id=1895 lang=cpp
 *
 * [1895] Largest Magic Square
 */

// @lc code=start
#include <vector>
using namespace std;

class Solution {
public:
    int largestMagicSquare(vector<vector<int>>& grid) {
        int m = grid.size();
        int n = grid[0].size();

        vector<vector<int>> rowSum(m, vector<int>(n + 1, 0));
        vector<vector<int>> colSum(m + 1, vector<int>(n, 0));
        vector<vector<int>> leftDiagonalSum(m + 1, vector<int>(n + 1, 0));
        vector<vector<int>> rightDiagonalSum(m + 1, vector<int>(n + 1, 0));

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                rowSum[i][j + 1] = rowSum[i][j] + grid[i][j];
                colSum[i + 1][j] = colSum[i][j] + grid[i][j];
                leftDiagonalSum[i + 1][j] = leftDiagonalSum[i][j + 1] + grid[i][j];
                rightDiagonalSum[i + 1][j + 1] = rightDiagonalSum[i][j] + grid[i][j];
            }
        }

        for (int k = min(m, n); k > 0; k--) {
            for (int i = m - 1; i >= k - 1; i--) {
                for (int j = n - 1; j >= k - 1; j--) {
                    int S = rightDiagonalSum[i + 1][j + 1] - rightDiagonalSum[i + 1 - k][j + 1 - k];
                    bool allS = true;
                    allS = allS && (leftDiagonalSum[i + 1][j + 1 - k] - leftDiagonalSum[i + 1 - k][j + 1] == S);
                    for (int l = i - k + 1; l <= i; l++) {
                        allS = allS && (rowSum[l][j + 1] - rowSum[l][j + 1 - k] == S);
                    }
                    for (int l = j - k + 1; l <= j; l++) {
                        allS = allS && (colSum[i + 1][l] - colSum[i + 1 - k][l] == S);
                    }
                    if (allS) {
                        return k;
                    }
                }
            }
        }
        return -1;
    }
};

// @lc code=end

