/*
 * @lc app=leetcode id=875 lang=csharp
 *
 * [875] Koko Eating Bananas
 */

// @lc code=start
using System.Linq;
using System;
public class Solution 
{
    public int MinEatingSpeed(int[] piles, int h) 
    {
        int left = 1;
        int right = piles.Max();
        while (left < right)
        {
            int mid = left + (right - left) / 2;
            if (piles.Select(x => x % mid == 0 ? x / mid : 1 + x / mid).Sum() > h)
            {
                left = 1 + mid;
            }
            else
            {
                right = mid;
            }
        }   
        return left;
    }
}
// @lc code=end

