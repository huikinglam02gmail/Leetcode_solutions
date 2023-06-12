/*
 * @lc app=leetcode id=1751 lang=csharp
 *
 * [1751] Maximum Number of Events That Can Be Attended II
 */

// @lc code=start
using System;
using System.Collections.Generic;
using System.Linq;

public class Solution
{
    /*
    DP problem. First sort events by starttime
    dp(i, j) = maximum sum of values that you can receive by attending events[i:], whereas you have j events left
    dp(i, j) = max(dp(i + 1, j), events[i][2] + dp(next available index, j - 1))
    skip event i or attend event i
    if j == 0: dp(i, j) = 0
    We are looking for dp(0, k)
    */

    public static int bisectRight<T>(IList<T> nums, T target, int left=0, int right=-1) where T : IConvertible, IComparable, IComparable<T>, IEquatable<T>
    {
        right = (right == -1) ? nums.Count : right;
        while (left < right)
        {
            int mid = left + (right - left) / 2;

            if (nums[mid].CompareTo(target) <= 0)
            {
                left = mid + 1;
            }
            else
            {
                right = mid;
            }
        }
        return left;
    }

    public int MaxValue(int[][] events, int k)
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
}

// @lc code=end
