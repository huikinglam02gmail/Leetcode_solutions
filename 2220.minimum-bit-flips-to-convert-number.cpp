/*
 * @lc app=leetcode id=2220 lang=cpp
 *
 * [2220] Minimum Bit Flips to Convert Number
 */

// @lc code=start
#include <bitset>

class Solution {
public:
    int minBitFlips(int start, int goal) {
        std::bitset<30> binStart(start);
        std::bitset<30> binGoal(goal);

        int result = 0;

        for (int i = 0; i < 30; ++i) {
            if (binStart[i] != binGoal[i]) {
                ++result;
            }
        }

        return result;
    }
};
// @lc code=end

