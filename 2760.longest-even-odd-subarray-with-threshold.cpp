/*
 * @lc app=leetcode id=2760 lang=cpp
 *
 * [2760] Longest Even Odd Subarray With Threshold
 */

// @lc code=start
#include <vector>

class Solution {
public:
    int longestAlternatingSubarray(std::vector<int>& nums, int threshold) {
        int n = nums.size();
        int result = 0;

        for (int i = 0; i < n; i++) {
            if (nums[i] % 2 == 0 && nums[i] <= threshold) {
                int j = i + 1;
                while (j < n && nums[j] % 2 != nums[j - 1] % 2 && nums[j] <= threshold) {
                    j++;
                }
                result = std::max(result, j - i);
            }
        }

        return result;
    }
};

// @lc code=end

