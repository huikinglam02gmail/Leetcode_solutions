/*
 * @lc app=leetcode id=3046 lang=cpp
 *
 * [3046] Split the Array
 */

// @lc code=start
#include <unordered_map>
#include <vector>

class Solution {
public:
    bool isPossibleToSplit(std::vector<int>& nums) {
        std::unordered_map<int, int> occur;
        for (int num : nums) {
            occur[num]++;
            if (occur[num] > 2) {
                return false;
            }
        }
        return true;
    }
};

// @lc code=end

