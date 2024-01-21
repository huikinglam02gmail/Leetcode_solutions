/*
 * @lc app=leetcode id=2553 lang=cpp
 *
 * [2553] Separate the Digits in an Array
 */

// @lc code=start
#include <vector>
#include <string>

class Solution {
public:
    std::vector<int> separateDigits(std::vector<int>& nums) {
        std::vector<int> result;
        for (int num : nums) {
            std::string numStr = std::to_string(num);
            for (char c : numStr) {
                result.push_back(c - '0');
            }
        }
        return result;
    }
};

// @lc code=end

