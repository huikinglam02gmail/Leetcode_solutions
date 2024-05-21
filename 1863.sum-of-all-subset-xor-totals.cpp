/*
 * @lc app=leetcode id=1863 lang=cpp
 *
 * [1863] Sum of All Subset XOR Totals
 */

// @lc code=start
#include <vector>

class Solution {
public:
    int subsetXORSum(std::vector<int>& nums) {
        int n = nums.size();
        int size = 1 << n;
        std::vector<int> dp(size, 0);
        int j = 0;

        for (int i = 1; i < size; i++) {
            if (i == (1 << (j + 1))) j++;
            dp[i] = dp[i - (1 << j)] ^ nums[j];
        }

        int sum = 0;
        for (int val : dp) {
            sum += val;
        }

        return sum;
    }
};

// @lc code=end

