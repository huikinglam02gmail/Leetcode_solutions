/*
 * @lc app=leetcode id=1074 lang=cpp
 *
 * [1074] Number of Submatrices That Sum to Target
 */

// @lc code=start
#include <vector>
#include <unordered_map>

class Solution {
public:
    int numSubmatrixSumTarget(std::vector<std::vector<int>>& matrix, int target) {
        int m = matrix.size();
        int n = matrix[0].size();

        std::vector<std::vector<int>> prefixSums(m + 1, std::vector<int>(n + 1, 0));
        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                prefixSums[i][j] = matrix[i - 1][j - 1];
                if (j > 1) prefixSums[i][j] += prefixSums[i][j - 1];
            }
        }

        int result = 0;
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j <= n; j++) {
                std::unordered_map<int, int> cumuSumSeen;
                int cumuSum = 0;

                for (int row = 1; row <= m; row++) {
                    cumuSum += prefixSums[row][j] - prefixSums[row][i];
                    if (cumuSum == target) {
                        result++;
                    }

                    if (cumuSumSeen.find(cumuSum - target) != cumuSumSeen.end()) {
                        result += cumuSumSeen[cumuSum - target];
                    }

                    cumuSumSeen[cumuSum]++;
                }
            }
        }

        return result;
    }
};

// @lc code=end

