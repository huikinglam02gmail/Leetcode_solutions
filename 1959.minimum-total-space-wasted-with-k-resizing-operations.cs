/*
 * @lc app=leetcode id=1959 lang=csharp
 *
 * [1959] Minimum Total Space Wasted With K Resizing Operations
 */

// @lc code=start
using System;

public class Solution {
    public int MinSpaceWastedKResizing(int[] nums, int k) {
        int n = nums.Length;
        int[] prefix = new int[n + 1];
        for (int i = 0; i < n; i++) 
        {
            prefix[i + 1] = prefix[i] + nums[i];
        }

        int[][] rangeMax = new int[n][];
        int[][] cost = new int[n][];
        for (int i = 0; i < n; i++) 
        {
            rangeMax[i] = new int[n];
            cost[i] = new int[n];
        }

        for (int i = 0; i < n; i++) 
        {
            for (int j = i; j < n; j++) 
            {
                if (j == i) 
                {
                    rangeMax[i][j] = nums[i];
                } else 
                {
                    rangeMax[i][j] = Math.Max(nums[j], rangeMax[i][j - 1]);
                }
                cost[i][j] = (j + 1 - i) * rangeMax[i][j] - prefix[j + 1] + prefix[i];
            }
        }

        int[][] dp = new int[k + 1][];
        for (int i = 0; i <= k; i++) {
            dp[i] = new int[n];
            dp[i] = dp[i].Select(x => Int32.MaxValue).ToArray();
        }

        for (int i = 0; i <= k; i++) 
        {
            for (int j = n - 1; j >= 0; j--)
            {
                if (i == 0) 
                {
                    dp[i][j] = cost[j][n - 1];
                }
                else 
                {
                    for (int l = j + 1; l <= n; l++) 
                    {
                        if (l < n) 
                        {
                            dp[i][j] = Math.Min(dp[i][j], dp[i - 1][l] + cost[j][l - 1]);
                        } 
                        else 
                        {
                            dp[i][j] = Math.Min(dp[i][j], cost[j][l - 1]);
                        }
                    }
                }
            }
        }

        return dp[k][0];
    }
}


// @lc code=end

