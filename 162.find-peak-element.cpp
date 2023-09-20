/*
 * @lc app=leetcode id=162 lang=cpp
 *
 * [162] Find Peak Element
 */

// @lc code=start
#include <vector>

class Solution {
public:
    int findPeakElement(std::vector<int>& nums) {
        int n = nums.size();
        if (n == 1) return 0;
        else if (n == 2) return nums[0] > nums[1] ? 0 : 1;
        else {
            int left = 0;
            int right = n;

            while (left < right) {
                int mid = left + (right - left) / 2;
                if ((mid == 0 || nums[mid - 1] < nums[mid]) && (mid == n - 1 || nums[mid + 1] < nums[mid])) {
                    return mid;
                } else if (nums[mid - 1] > nums[mid]) {
                    right = mid;
                } else {
                    left = mid + 1;
                }
            }

            return left;
        }
    }
};

// @lc code=end

