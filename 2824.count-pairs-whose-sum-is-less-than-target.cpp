/*
 * @lc app=leetcode id=2824 lang=cpp
 *
 * [2824] Count Pairs Whose Sum is Less than Target
 */

// @lc code=start
#include <vector>
#include <algorithm>

class Solution {
public:
    int countPairs(std::vector<int>& nums, int target) {
        std::sort(nums.begin(), nums.end());
        int result = 0;
        for (int i = 0; i < nums.size(); i++) {
            int ind = std::lower_bound(nums.begin() + i + 1, nums.end(), target - nums[i]) - nums.begin();
            result += std::max(0, ind - i - 1);
        }
        return result;
    }
};

// @lc code=end

