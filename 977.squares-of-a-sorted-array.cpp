/*
 * @lc app=leetcode id=977 lang=cpp
 *
 * [977] Squares of a Sorted Array
 */

// @lc code=start
#include <vector>
#include <algorithm>

class Solution {
public:
    std::vector<int> sortedSquares(std::vector<int>& nums) {
        std::sort(nums.begin(), nums.end(), [](int x, int y) {
            return x * x < y * y;
        });
        
        for (int& num : nums) {
            num *= num;
        }
        
        return nums;
    }
};

// @lc code=end

