/*
 * @lc app=leetcode id=153 lang=cpp
 *
 * [153] Find Minimum in Rotated Sorted Array
 */

// @lc code=start
#include <vector>

class Solution {
public:
    int findMin(std::vector<int>& nums) {
        int l = 0;
        int r = nums.size();
        while (l < r - 1) {
            int mid = l + (r - l) / 2;
            if (nums[mid] > nums[l]) {
                l = mid;
            } else {
                r = mid;
            }
        }
        return nums[(l + 1) % nums.size()];
    }
};

// @lc code=end

