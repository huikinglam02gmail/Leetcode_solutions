/*
 * @lc app=leetcode id=486 lang=csharp
 *
 * [486] Predict the Winner
 */

// @lc code=start
using System;

public class Solution
{
    /*
     * Use DP to find the winner.
     * dp[i][j] = maximum score difference between player 1 and player 2 if nums[i:j + 1] is left behind and it's player 1's turn.
     */
    public bool PredictTheWinner(int[] nums)
    {
        int n = nums.Length;
        int[,] dp = new int[n, n];

        for (int j = 0; j < n; j++)
        {
            for (int i = j; i >= 0; i--)
            {
                if (i == j)
                {
                    dp[i, j] = nums[i];
                }
                else
                {
                    dp[i, j] = Math.Max(nums[i] - dp[i + 1, j], nums[j] - dp[i, j - 1]);
                }
            }
        }

        return dp[0, n - 1] >= 0;
    }
}

// @lc code=end

