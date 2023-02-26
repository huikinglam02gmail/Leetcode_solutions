/*
 * @lc app=leetcode id=1011 lang=csharp
 *
 * [1011] Capacity To Ship Packages Within D Days
 */

// @lc code=start
using System.Collections.Generic;
using System;
using System.Linq;
public class Solution 
{
    List<int> prefix = new List<int>() {0};
    
    private int getdays(int capacity)
    {
        int day = 0;
        int i = 0;
        int j = 0;
        while (i < prefix.Count)
        {
            while (j < prefix.Count && prefix[j] - prefix[i] <= capacity)
            {
                j++;
            }
            if (j < prefix.Count && prefix[j] - prefix[i] > capacity)
            {
                i = j - 1;
            }
            else
            {
                i = j;
            }
            day++;
       }
       return day;
    }

    public int ShipWithinDays(int[] weights, int days) 
    {
        foreach (int weight in weights)
        {
            prefix.Add(prefix[prefix.Count - 1] + weight);
        }

        int left = weights.Max();
        int right = prefix[prefix.Count - 1];
        while (left < right)
        {
            int mid = left + (right - left) / 2;
            if (getdays(mid) <= days)
            {
                right = mid;
            }            
            else
            {
                left = mid + 1;
            }
        }
        return left;
    }
}
// @lc code=end

