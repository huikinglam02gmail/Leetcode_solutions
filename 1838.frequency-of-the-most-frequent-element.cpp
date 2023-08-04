/*
 * @lc app=leetcode id=1838 lang=cpp
 *
 * [1838] Frequency of the Most Frequent Element
 */

// @lc code=start
#include <algorithm>
#include <vector>

class Solution {
public:
    int maxFrequency(std::vector<int>& nums, int k) {
        std::sort(nums.begin(), nums.end());
        std::vector<long> prefix = { 0 };
        for (int num : nums) {
            prefix.push_back(prefix.back() + num);
        }
        int result = 0;
        int j = 0;
        int n = nums.size();
        for (int i = 0; i < n; i++) {
            while ((long long)(i - j) * (long long)nums[i] - (long long) prefix[i] + (long long)prefix[j] > (long long)k) {
                j++;
            }
            result = std::max(result, i + 1 - j);
        }
        return result;
    }
};

// @lc code=end

