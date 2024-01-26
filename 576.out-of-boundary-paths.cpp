/*
 * @lc app=leetcode id=576 lang=cpp
 *
 * [576] Out of Boundary Paths
 */

// @lc code=start
#include <vector>
#include <map>

class Solution {
public:
    /**
     * DP problem
     * Count the number of times the ball can arrive at the edge for each number of moves
     */
    int scores(int row, int col, int m, int n) {
        int count = 0;
        if (row == 0) {
            count += 1;
        }
        if (col == 0) {
            count += 1;
        }
        if (row == m - 1) {
            count += 1;
        }
        if (col == n - 1) {
            count += 1;
        }
        return count;
    }

    int findPaths(int m, int n, int maxMove, int startRow, int startColumn) {
        long long MOD = 1000000007;
        std::vector<std::vector<long long>> dp(m, std::vector<long long>(n, 0));

        // Get the coordinates of hash map of corners and edges to store the number of exit ways
        std::map<std::pair<int, int>, long long> hashTable;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                int score = scores(i, j, m, n);
                if (score > 0) {
                    hashTable[{i, j}] = score;
                }
            }
        }

        long long result = 0;
        // Keep counting numbers of balls possible in each position
        // Count the edge and corners scores * the dp count
        for (int move = 0; move < maxMove; move++) {
            if (move == 0) {
                dp[startRow][startColumn] = 1;
                if (hashTable.count({startRow, startColumn}) > 0) {
                    result += hashTable[{startRow, startColumn}];
                    result %= MOD;
                }
            } else {
                std::vector<std::vector<long long>> dpNew(m, std::vector<long long>(n, 0));
                for (int i = 0; i < m; i++) {
                    for (int j = 0; j < n; j++) {
                        if (i >= 1) {
                            dpNew[i][j] += dp[i - 1][j];
                            dpNew[i][j] %= MOD;
                        }
                        if (j >= 1) {
                            dpNew[i][j] += dp[i][j - 1];
                            dpNew[i][j] %= MOD;
                        }
                        if (i < m - 1) {
                            dpNew[i][j] += dp[i + 1][j];
                            dpNew[i][j] %= MOD;
                        }
                        if (j < n - 1) {
                            dpNew[i][j] += dp[i][j + 1];
                            dpNew[i][j] %= MOD;
                        }
                        if (hashTable.count({i, j}) > 0) {
                            result += dpNew[i][j] * hashTable[{i, j}];
                            result %= MOD;
                        }
                    }
                }
                dp = dpNew;
            }
        }

        return static_cast<int>(result);
    }
};

// @lc code=end

