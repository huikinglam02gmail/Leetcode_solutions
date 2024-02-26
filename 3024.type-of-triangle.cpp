/*
 * @lc app=leetcode id=3024 lang=cpp
 *
 * [3024] Type of Triangle
 */

// @lc code=start
#include <vector>
#include <algorithm>
#include <unordered_set>
#include <string>

class Solution {
public:
    std::string triangleType(std::vector<int>& nums) {
        std::sort(nums.begin(), nums.end());
        if (nums[0] + nums[1] <= nums[2]) {
            return "none";
        }
        std::unordered_set<int> distinctNums(nums.begin(), nums.end());
        int distinctCount = distinctNums.size();
        if (distinctCount == 1) {
            return "equilateral";
        } else if (distinctCount == 2) {
            return "isosceles";
        } else if (distinctCount == 3) {
            return "scalene";
        } else {
            throw std::invalid_argument("Invalid input");
        }
    }
};

// @lc code=end

