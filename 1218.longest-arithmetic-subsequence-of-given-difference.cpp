/*
 * @lc app=leetcode id=1218 lang=cpp
 *
 * [1218] Longest Arithmetic Subsequence of Given Difference
 */

// @lc code=start
#include<vector>
#include<unordered_map>
#include<algorithm>
using std::max;
using std::unordered_map;
using std::vector;
class Solution {
public:
    int longestSubsequence(vector<int>& arr, int difference) {
        unordered_map<int, int> dp{};
        int maxSeen = 0;
        
        for (int num : arr) {
            dp.emplace(num, 0);
            dp.emplace(num - difference, 0);
            dp[num] = max(dp[num], 1 + dp[num - difference]);
            maxSeen = max(maxSeen, dp[num]);
        }
        
        return maxSeen;        
    }
};
// @lc code=end

