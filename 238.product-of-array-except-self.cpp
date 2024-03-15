/*
 * @lc app=leetcode id=238 lang=cpp
 *
 * [238] Product of Array Except Self
 */

// @lc code=start
#include <vector>

class Solution {
public:
    std::vector<int> productExceptSelf(std::vector<int>& nums) {
        int n = nums.size();
        std::vector<int> result(n, 1);
        
        for (int i = 1; i < n; i++) {
            result[i] = result[i - 1] * nums[i - 1];
        }

        int last = nums[n - 1];
        for (int i = n - 2; i >= 0; i--) {
            result[i] *= last;
            last *= nums[i];
        }
        
        return result;
    }
};

// @lc code=end

