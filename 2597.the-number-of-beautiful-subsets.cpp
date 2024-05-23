/*
 * @lc app=leetcode id=2597 lang=cpp
 *
 * [2597] The Number of Beautiful Subsets
 */

// @lc code=start
#include <vector>
#include <unordered_map>
#include <algorithm>
#include <cmath>

class Solution {
public:
    /*
     * Separate nums into different groups according to num % k.
     * Among different groups, we can combine eligible subsets without any issue, 
     * i.e., multiply them together will give the answer.
     * Inside each group, we first sort the numbers appearing and count how many times it occurs.
     * Then we need to keep track of two dp numbers:
     * 1. dp0[i] = number of subsets which do not include a[i]
     * 2. dp1[i] = number of subsets which includes a[i]
     * Given a[i + 1], dp0[i + 1] = dp0[i] + dp1[i]
     * if a[i] == a[i + 1] - k: dp1[i + 1] = dp0[i] * 2 ^ (count[j][a[i + 1]] - 1)
     * else: dp1[i + 1] = (dp0[i] + dp1[i]) * 2 ^ (count[j][a[i + 1]] - 1)
     * Power of 2 because subset could include / not include each occurrence of a[i + 1].
     */
    int beautifulSubsets(std::vector<int>& nums, int k) {
        std::vector<std::unordered_map<int, int>> counts(k);
        for (int num : nums) {
            counts[num % k][num]++;
        }
        
        int res = 1;
        for (int i = 0; i < k; i++) {
            int prev = 0, dp0 = 1, dp1 = 0;
            std::vector<int> keys;
            for (const auto& pair : counts[i]) {
                keys.push_back(pair.first);
            }
            std::sort(keys.begin(), keys.end());
            
            for (int a : keys) {
                int ways = (1 << counts[i][a]) - 1;
                int dp0New = dp0 + dp1;
                int dp1New = ways;
                if (prev == a - k) {
                    dp1New *= dp0;
                } else {
                    dp1New *= (dp0 + dp1);
                }
                prev = a;
                dp0 = dp0New;
                dp1 = dp1New;
            }
            res *= (dp0 + dp1);
        }
        return res - 1;
    }
};

// @lc code=end

