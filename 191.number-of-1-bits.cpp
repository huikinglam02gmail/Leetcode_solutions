/*
 * @lc app=leetcode id=191 lang=cpp
 *
 * [191] Number of 1 Bits
 */

// @lc code=start
#include <bitset>

class Solution {
public:
    int hammingWeight(uint32_t n) {
        return std::bitset<32>(n).count();
    }
};

// @lc code=end

