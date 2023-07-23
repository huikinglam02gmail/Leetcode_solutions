/*
 * @lc app=leetcode id=1824 lang=cpp
 *
 * [1824] Minimum Sideway Jumps
 */

// @lc code=start
#include <vector>
#include <algorithm>
using std::copy;
using std::min;
using std::min_element;
using std::vector;

class Solution {
public:
    /*
    Number of states are limited at each position
    dp[i][j] = number of side jumps needed to reach at (i, j)
    dp[i][j] = min(dp[i - 1][j], 1 + dp[i][k != j]) if obstable[i] != k
    We aim to get min(dp[n][:]) 
    */
    int minSideJumps(vector<int>& obstacles) {
        int n = obstacles.size();
        vector<int> dp1 = { 1, 0, 1 };
        vector<int> dp2(3, 0);
        vector<int> dp3(3, 0);
        
        for (int i = 0; i < n; i++) {
            copy(dp1.begin(), dp1.end(), dp2.begin());
            
            if (obstacles[i] > 0) {
                dp2[obstacles[i] - 1] = 1000000; // Similar to int.MaxValue
            }
            
            copy(dp2.begin(), dp2.end(), dp3.begin());
            
            for (int j = 0; j < 2; j++) {
                for (int k = j + 1; k < 3; k++) {
                    if (obstacles[i] - 1 != j) {
                        dp3[j] = min(dp3[j], 1 + dp2[k]);
                    }
                    if (obstacles[i] - 1 != k) {
                        dp3[k] = min(dp3[k], 1 + dp2[j]);
                    }
                }
            }
            
            copy(dp3.begin(), dp3.end(), dp1.begin());
        }
        
        return *min_element(dp1.begin(), dp1.end());
    }
};

// @lc code=end

