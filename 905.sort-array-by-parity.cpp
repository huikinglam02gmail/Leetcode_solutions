/*
 * @lc app=leetcode id=905 lang=cpp
 *
 * [905] Sort Array By Parity
 */

// @lc code=start
#include <vector>
#include <algorithm>

class Solution {
public:
    std::vector<int> sortArrayByParity(std::vector<int>& nums) {
        std::sort(nums.begin(), nums.end(), [](int x, int y) { return x % 2 < y % 2; });
        return nums;
    }
};

// @lc code=end

