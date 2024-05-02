/*
 * @lc app=leetcode id=2441 lang=cpp
 *
 * [2441] Largest Positive Integer That Exists With Its Negative
 */

// @lc code=start
#include <vector>
#include <algorithm>
#include <unordered_set>

class Solution {
public:
    int findMaxK(std::vector<int>& nums) {
        std::sort(nums.begin(), nums.end());
        std::unordered_set<int> numsSet(nums.begin(), nums.end());
        int p = nums.size() - 1;
        while (p >= 0 && nums[p] > 0) {
            if (numsSet.count(-nums[p])) return nums[p];
            p--;
        }
        return -1;
    }
};

// @lc code=end

