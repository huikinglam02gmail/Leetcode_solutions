/*
 * @lc app=leetcode id=34 lang=cpp
 *
 * [34] Find First and Last Position of Element in Sorted Array
 */

// @lc code=start
#include <vector>
#include <algorithm>

using std::lower_bound;
using std::upper_bound;
using std::vector;

class Solution {
public:
    vector<int> searchRange(vector<int>& nums, int target) 
    {
        if (nums.size() > 0)
        {
            int left = lower_bound(nums.begin(), nums.end(), target) - nums.begin();
            if (left < nums.size() && nums[left] == target)
            {
                return vector<int> {left, (int) (upper_bound(nums.begin(), nums.end(), target) - nums.begin()) - 1};
            }            
        }
        return vector<int> {-1, -1};
    }
};

// @lc code=end

