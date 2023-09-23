/*
 * @lc app=leetcode id=1911 lang=cpp
 *
 * [1911] Maximum Alternating Subsequence Sum
 */

// @lc code=start
#include <vector>
#include <algorithm>

using std::max;
using std::vector;

class Solution {
public:
    long long maxAlternatingSum(vector<int>& nums) {
        long long result = nums[0];
        
        for (int i = 0; i < nums.size() - 1; i++) {
            result += max((long long)0, (long long)(nums[i + 1] - nums[i]));
        }
        
        return result;
    }
};

// @lc code=end

