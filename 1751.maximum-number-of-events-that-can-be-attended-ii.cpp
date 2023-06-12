/*
 * @lc app=leetcode id=1751 lang=cpp
 *
 * [1751] Maximum Number of Events That Can Be Attended II
 */

// @lc code=start
#include <vector>;
using std::vector;
class Solution {
public:
    int maxValue(vector<vector<int>>& events, int k) 
    {
        events = events.OrderBy(x => x[0]).ToArray();
        int[] startingPoints = events.Select(x => x[0]).ToArray();
        int n = events.Length;
        int[,] dp = new int[n, k + 1];
        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < k + 1; j++)
            {
                dp[i, j] = 0;
            }
        }

        for (int i = n - 1; i >= 0; i--)
        {
            for (int j = 1; j <= k; j++)
            {
                if (i < n - 1)
                {
                    dp[i, j] = dp[i + 1, j];                    
                }
                int nxtInd = bisectRight<int>(startingPoints, events[i][1]);
                dp[i, j] = Math.Max(dp[i, j], events[i][2] + (nxtInd < n ? dp[nxtInd, j - 1] : 0));
            }
        }
        return dp[0, k];  
    }
};
// @lc code=end

