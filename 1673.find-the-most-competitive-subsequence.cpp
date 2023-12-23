/*
 * @lc app=leetcode id=1673 lang=cpp
 *
 * [1673] Find the Most Competitive Subsequence
 */

// @lc code=start
#include <vector>

class Solution {
public:
    std::vector<int> mostCompetitive(std::vector<int>& nums, int k) {
        std::vector<int> stack;
        int n = nums.size();

        for (int i = 0; i < n; i++) {
            while (!stack.empty() && nums[i] < stack.back() && n - i + stack.size() - 1 >= k) {
                stack.pop_back();
            }
            stack.push_back(nums[i]);
        }

        return std::vector<int>(stack.begin(), stack.begin() + k);
    }
};

// @lc code=end

