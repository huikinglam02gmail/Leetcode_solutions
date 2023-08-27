/*
 * @lc app=leetcode id=1877 lang=cpp
 *
 * [1877] Minimize Maximum Pair Sum in Array
 */

// @lc code=start
#include <vector>
#include <algorithm>

class Solution {
public:
    int minPairSum(std::vector<int>& nums) {
        std::sort(nums.begin(), nums.end());
        int i = 0, j = nums.size() - 1;
        int result = 0;
        while (i < j) {
            result = std::max(result, nums[i] + nums[j]);
            i++;
            j--;
        }
        return result;
    }
};
// @lc code=end

