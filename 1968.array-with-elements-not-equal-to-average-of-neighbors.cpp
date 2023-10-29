/*
 * @lc app=leetcode id=1968 lang=cpp
 *
 * [1968] Array With Elements Not Equal to Average of Neighbors
 */

// @lc code=start
#include <vector>
#include <algorithm>

class Solution {
public:
    std::vector<int> rearrangeArray(std::vector<int>& nums) {
        int n = nums.size();
        std::sort(nums.begin(), nums.end());
        std::vector<int> result(n, 0);
        for (int i = 0; i < n; i += 2) {
            result[i] = nums[n - 1 - i / 2];
        }
        for (int i = 1; i < n; i += 2) {
            result[i] = nums[i / 2];
        }
        return result;
    }
};

// @lc code=end

