/*
 * @lc app=leetcode id=435 lang=csharp
 *
 * [435] Non-overlapping Intervals
 */

// @lc code=start
using System;
using System.Collections.Generic;

public class Solution
{
    /*
     * The minimum number of intervals you need to remove is equal to
     * n - the maximum length of non-overlapping intervals.
     * We can first sort intervals by the second index
     * (Earlier ending ones leave room for future ones to fill in).
     */

    public int EraseOverlapIntervals(int[][] intervals)
    {
        Array.Sort(intervals, (x, y) => x[1].CompareTo(y[1]));
        int n = intervals.Length;
        List<int[]> result = new List<int[]>();
        int ans = 0;

        foreach (int[] interval in intervals)
        {
            if (result.Count > 0 && interval[0] < result[result.Count - 1][1])
            {
                ans++;
            }
            else
            {
                result.Add(interval);
            }
        }

        return ans;
    }
}

// @lc code=end

