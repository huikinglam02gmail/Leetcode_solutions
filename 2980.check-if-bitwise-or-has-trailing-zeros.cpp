/*
 * @lc app=leetcode id=2980 lang=cpp
 *
 * [2980] Check if Bitwise OR Has Trailing Zeros
 */

// @lc code=start
#include <vector>

class Solution {
public:
    bool hasTrailingZeros(std::vector<int>& nums) {
        int count = 0;
        for (int num : nums) {
            if (num % 2 == 0) {
                count++;
            }
        }
        return count > 1;
    }
};

// @lc code=end

