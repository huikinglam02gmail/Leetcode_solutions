/*
 * @lc app=leetcode id=209 lang=cpp
 *
 * [209] Minimum Size Subarray Sum
 */

// @lc code=start
#include<vector>
#include<algorithm>
using std::lower_bound;
using std::min;
using std::vector;
class Solution {
public:
    int minSubArrayLen(int target, vector<int>& nums) {
        vector<int> prefix{0};
        for (int num : nums)
        {
            prefix.push_back(num + prefix.back());
        }

        int result = prefix.size();
        for (int i = 0; i < prefix.size() - 1; i++)
        {
            int index = lower_bound(prefix.begin(), prefix.end(), prefix[i] + target) - prefix.begin();
            if (index < prefix.size())
            {
                result = min(result, index - i);
            }
        }

        return result < prefix.size() ? result : 0;        
    }
};
// @lc code=end

