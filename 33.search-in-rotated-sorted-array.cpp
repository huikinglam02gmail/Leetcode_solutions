/*
 * @lc app=leetcode id=33 lang=cpp
 *
 * [33] Search in Rotated Sorted Array
 */

// @lc code=start
#include <vector>
#include <algorithm>
using std::lower_bound;
using std::vector;
class Solution {
public:
    int FindMin(std::vector<int>& nums) {
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
        return (l + 1) % nums.size();
    }

    int search(std::vector<int>& nums, int target) {
        if (nums[0] == target) {
            return 0;
        } else if (nums[nums.size() - 1] == target) {
            return nums.size() - 1;
        } else {
            int ind = FindMin(nums);
            int result;
            if (ind > 0 && nums[0] < target) {
                result = lower_bound(nums.begin(), nums.begin() + ind, target) - nums.begin();
            } else {
                result = lower_bound(nums.begin() + ind, nums.end(), target) - nums.begin();
            }
            return (result == nums.size() || nums[result] != target) ? -1 : result;
        }
    }
};
// @lc code=end

