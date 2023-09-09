/*
 * @lc app=leetcode id=377 lang=cpp
 *
 * [377] Combination Sum IV
 */

// @lc code=start

#include <vector>
#include <algorithm>

using std::sort;
using std::upper_bound;
using std::vector;

class Solution {
public:
    int combinationSum4(std::vector<int>& nums, int target) 
    {
        sort(nums.begin(), nums.end());
        vector<long long> dp(target + 1, (long long)0);
        long long MOD = 10000000007;
        dp[0] = (long long)1;

        for (int i = nums[0]; i <= target; i++) 
        {
            int limit = upper_bound(nums.begin(), nums.end(), i) - nums.begin();
            for (int j = 0; j < limit; j++) 
            {      
                dp[i] += dp[i - nums[j]];
                dp[i] %= MOD;
            }
        }

        return (int)dp[target];
    }
};

// @lc code=end

