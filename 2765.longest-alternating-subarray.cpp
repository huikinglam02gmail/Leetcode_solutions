/*
 * @lc app=leetcode id=2765 lang=cpp
 *
 * [2765] Longest Alternating Subarray
 */

// @lc code=start
#include <vector>

class Solution {
public:
    int alternatingSubarray(std::vector<int>& nums) {
        int n = nums.size();
        int result = 1;

        for (int i = 0; i < n - 1; i++) {
            int j = i + 1;
            int p = 0;
            while (j < n && nums[j] == nums[j - 1] + pow(-1, p)) {
                p++;
                j++;
            }
            
            if (nums[j - 1] == nums[i] || nums[j - 1] == nums[i] + 1) {
                result = std::max(result, j - i);
            }
        }

        return result > 1 ? result : -1;
    }
};

// @lc code=end

