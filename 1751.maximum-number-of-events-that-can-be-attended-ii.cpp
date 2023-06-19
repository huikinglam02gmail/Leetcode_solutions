/*
 * @lc app=leetcode id=1751 lang=cpp
 *
 * [1751] Maximum Number of Events That Can Be Attended II
 */

// @lc code=start
#include <vector>
#include <algorithm>
using std::max;
using std::sort;
using std::transform;
using std::upper_bound;
using std::vector;

class Solution {
private:
    int getFirst(vector<int> arr){
        return arr.front();
    };

public:
    int maxValue(vector<vector<int>>& events, int k) 
    {
        sort(events.begin(), events.end());
        vector<int> startingPoints{};
        for (vector<int> event : events)
        {
            startingPoints.push_back(event.front());
        }
        int n = events.size();
        vector<vector<int>> dp;
        dp.resize(n, vector<int>(k + 1, 0));
        int nxtInd;

        for (int i = n - 1; i >= 0; i--)
        {
            for (int j = 1; j <= k; j++)
            {
                if (i < n - 1)
                {
                    dp[i][j] = dp[i + 1][j];                    
                }
                nxtInd = upper_bound(startingPoints.begin(), startingPoints.end(), events[i][1]) - startingPoints.begin();
                dp[i][j] = max(dp[i][j], events[i][2] + (nxtInd < n ? dp[nxtInd][j - 1] : 0));
            }
        }
        return dp[0][k];  
    }
};
// @lc code=end

