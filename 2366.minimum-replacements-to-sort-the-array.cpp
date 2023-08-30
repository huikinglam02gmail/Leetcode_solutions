/*
 * @lc app=leetcode id=2366 lang=cpp
 *
 * [2366] Minimum Replacements to Sort the Array
 */

// @lc code=start
#include <vector>

class Solution {
public:
    long long CeilDiv(long i, long j) {
        return (i + j - 1) / j;
    }

    long long minimumReplacement(std::vector<int>& nums) {
        long long remainder = nums[nums.size() - 1];
        int n = nums.size();
        long long result = 0;
        
        for (int i = n - 2; i >= 0; i--) {
            result += CeilDiv(nums[i], remainder) - 1;
            remainder = static_cast<long long>(nums[i]) / CeilDiv(nums[i], remainder);
        }
        
        return result;
    }
};
// @lc code=end

