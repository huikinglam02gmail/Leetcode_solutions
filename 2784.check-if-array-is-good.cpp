/*
 * @lc app=leetcode id=2784 lang=cpp
 *
 * [2784] Check if Array is Good
 */

// @lc code=start
#include <vector>
#include <algorithm>

class Solution {
public:
    bool isGood(std::vector<int>& nums) {
        int n = nums.size();
        std::sort(nums.begin(), nums.end());

        for (int i = 0; i < n - 1; i++) {
            if (nums[i] != i + 1) {
                return false;
            }
        }

        return nums[n - 1] == n - 1;
    }
};

// @lc code=end

