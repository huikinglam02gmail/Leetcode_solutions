/*
 * @lc app=leetcode id=2033 lang=cpp
 *
 * [2033] Minimum Operations to Make a Uni-Value Grid
 */

// @lc code=start
#include <vector>
#include <algorithm>
#include <cmath>

class Solution {
public:
    int minOperations(std::vector<std::vector<int>>& grid, int x) {
        int m = grid.size();
        int n = grid[0].size();

        std::vector<int> nums;

        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                nums.push_back(grid[i][j]);
            }
        }

        std::sort(nums.begin(), nums.end());

        if (x > 1) {
            for (int i = 1; i < m * n; i++) {
                if ((nums[i] - nums[0]) % x != 0) {
                    return -1;
                }
            }
        }

        int result = 0;
        int targetIndex = m * n / 2;

        for (int num : nums) {
            result += std::abs(num - nums[targetIndex]) / x;
        }

        return result;
    }
};

// @lc code=end

