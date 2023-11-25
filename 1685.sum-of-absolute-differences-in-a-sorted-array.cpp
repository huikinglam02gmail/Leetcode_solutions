/*
 * @lc app=leetcode id=1685 lang=cpp
 *
 * [1685] Sum of Absolute Differences in a Sorted Array
 */

// @lc code=start
#include <vector>

class Solution {
public:
    /*
     * For nums[i], smaller number nums[j] would give nums[i] - nums[j] and
     * larger number nums[k] would give nums[k] - nums[i].
     * So what we need is the sum of (i * nums[i] - sum(nums[:i])) +
     * (sum(nums[i+1:]) - (n - i) * nums[i]).
     * The sum can be handled by prefix sum.
     */
    std::vector<int> getSumAbsoluteDifferences(std::vector<int>& nums) {
        std::vector<int> prefix{0};
        for (int num : nums) {
            prefix.push_back(prefix.back() + num);
        }

        std::vector<int> result;
        int n = nums.size();
        for (int i = 0; i < n; ++i) {
            result.push_back((2 * i - n) * nums[i] - 2 * prefix[i] + prefix.back());
        }
        return result;
    }
};

// @lc code=end

