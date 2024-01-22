/*
 * @lc app=leetcode id=2574 lang=cpp
 *
 * [2574] Left and Right Sum Differences
 */

// @lc code=start
#include <vector>

class Solution {
public:
    /**
     * Prefix Sum
     */
    std::vector<int> leftRightDifference(std::vector<int>& nums) {
        std::vector<int> prefixSum = {0};
        for (int num : nums) {
            prefixSum.push_back(prefixSum.back() + num);
        }

        std::vector<int> result;
        for (int i = 0; i < nums.size(); i++) {
            result.push_back(std::abs(prefixSum.back() - prefixSum[i + 1] - prefixSum[i]));
        }

        return result;
    }
};

// @lc code=end

