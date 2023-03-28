/*
 * @lc app=leetcode id=983 lang=csharp
 *
 * [983] Minimum Cost For Tickets
 */

// @lc code=start
using System.Collections.Generic;
using System;
public class Solution 
{
    int[] Days;
    int[] Costs;
    int[] memo;

    public static int bisectLeft(int[] arr, int x)
    {
        int lo = 0;
        int hi = arr.Length;
        while (lo < hi)
        {
            int mid = lo + (hi - lo) / 2;
            if (arr[mid] < x)
            {
                lo = mid + 1;
            }
            else
            {
                hi = mid;
            }
        }
        return lo;     
    }
    public int dfs(int i)
    {
        if (i == Days.Length)
        {
            return 0;
        }
        else if (memo[i] == Int32.MaxValue)
        {
            memo[i] = Math.Min(memo[i], Costs[0] + dfs(i + 1));
            memo[i] = Math.Min(memo[i], Costs[1] + dfs(bisectLeft(Days, Days[i] + 7)));
            memo[i] = Math.Min(memo[i], Costs[2] + dfs(bisectLeft(Days, Days[i] + 30)));            
        }
        return memo[i];
    }

    public int MincostTickets(int[] days, int[] costs) 
    {
        Days = days;
        Costs = costs;
        memo = new int[days.Length];
        Array.Fill(memo, Int32.MaxValue);
        return dfs(0);
    }
}
// @lc code=end

