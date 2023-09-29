/*
 * @lc app=leetcode id=896 lang=cpp
 *
 * [896] Monotonic Array
 */

// @lc code=start
#include <vector>

class Solution {
public:
    bool isMonotonic(std::vector<int>& nums) {
        int direction = 0;
        for (int i = 0; i < nums.size() - 1; i++) {
            if (direction == 0) {
                if (nums[i + 1] > nums[i]) {
                    direction = 1;
                } else if (nums[i + 1] < nums[i]) {
                    direction = -1;
                }
            } else {
                if (nums[i + 1] > nums[i] && direction != 1) {
                    return false;
                } else if (nums[i + 1] < nums[i] && direction != -1) {
                    return false;
                }
            }
        }
        return true;
    }
};

// @lc code=end

