/*
 * @lc app=leetcode id=1872 lang=cpp
 *
 * [1872] Stone Game VIII
 */

// @lc code=start
#include <vector>

class Solution {
public:
    int stoneGameVIII(std::vector<int>& stones) {
        int dp = 0;
        int total = 0;
        int n = stones.size();
        
        for (int i = 0; i < n; i++) {
            total += stones[i];
        }
        
        dp = total;
        
        for (int i = n - 2; i > 0; i--) {
            total -= stones[i + 1];
            dp = std::max(dp, total - dp);
        }
        
        return dp;
    }
};

// @lc code=end

