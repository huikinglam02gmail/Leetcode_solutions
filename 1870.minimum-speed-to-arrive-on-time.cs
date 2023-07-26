/*
 * @lc app=leetcode id=1870 lang=csharp
 *
 * [1870] Minimum Speed to Arrive on Time
 */

// @lc code=start
using System;
using System.Collections.Generic;

public class Solution
{
    private int[] dist;
    private double hour;

    private double TimeToReach(int speed)
    {
        double result = 0;
        for (int i = 0; i < dist.Length - 1; i++)
        {
            result += (dist[i] + speed - 1) / speed;
        }
        return (double)result + (double)dist.Last() / (double)speed;
    }

    public int MinSpeedOnTime(int[] dist, double hour)
    {
        this.dist = dist;
        this.hour = hour;
        int maxDist = dist.Max();

        int l = 1, r = maxDist * 100 + 1;
        while (l < r)
        {
            int mid = l + (r - l) / 2;
            if (TimeToReach(mid) > hour)
            {
                l = mid + 1;
            }
            else
            {
                r = mid;
            }
        }
        return l == maxDist * 100 + 1 ? -1 : l;
    }
}

// @lc code=end

