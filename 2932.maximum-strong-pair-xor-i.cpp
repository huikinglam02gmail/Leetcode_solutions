/*
 * @lc app=leetcode id=2932 lang=cpp
 *
 * [2932] Maximum Strong Pair XOR I
 */

// @lc code=start
#include <vector>
#include <algorithm>

class Solution {
public:
    int maximumStrongPairXor(std::vector<int>& nums) {
        int result = 0;
        for (int num1 : nums) {
            for (int num2 : nums) {
                if (std::abs(num1 - num2) <= std::min(num1, num2)) {
                    result = std::max(result, num1 ^ num2);
                }
            }
        }
        return result;
    }
};

// @lc code=end

