/*
 * @lc app=leetcode id=287 lang=cpp
 *
 * [287] Find the Duplicate Number
 */

// @lc code=start
#include <vector>

class Solution {
public:
    int findDuplicate(std::vector<int>& nums) {
        int slow = 0, fast = 0;
        bool match = false;

        while (!match) {
            slow = nums[slow];
            fast = nums[nums[fast]];

            match = (slow == fast);
        }

        slow = 0;
        if (nums[slow] != nums[fast]) {
            match = false;

            while (!match) {
                slow = nums[slow];
                fast = nums[fast];
                match = (nums[slow] == nums[fast]);
            }
        }

        return nums[slow];
    }
};

// @lc code=end

