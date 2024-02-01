/*
 * @lc app=leetcode id=2966 lang=cpp
 *
 * [2966] Divide Array Into Arrays With Max Difference
 */

// @lc code=start
#include <vector>
#include <algorithm>

class Solution {
public:
    std::vector<std::vector<int>> divideArray(std::vector<int>& nums, int k) {
        std::sort(nums.begin(), nums.end());
        std::vector<std::vector<int>> result;
        int n = nums.size();

        for (int i = 0; i < n; i += 3) {
            if (i + 2 < n && nums[i + 2] - nums[i] > k) {
                return {}; // Return an empty vector if the condition is not satisfied
            } else {
                result.push_back({nums[i], nums[i + 1], nums[i + 2]});
            }
        }

        return result;
    }
};

// @lc code=end

