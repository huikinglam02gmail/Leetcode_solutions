/*
 * @lc app=leetcode id=2300 lang=csharp
 *
 * [2300] Successful Pairs of Spells and Potions
 */

// @lc code=start
using System;
using System.Collections.Generic;
public class Solution 
{
    public static int bisectRight(int[] nums, long target)
    {
        int left = 0;
        int right = nums.Length;
        while (left < right)
        {
            int mid = left + (right - left) / 2;

            if (nums[mid] <= target)
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

    public static int bisectLeft(int[] arr, long x)
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

    public int[] SuccessfulPairs(int[] spells, int[] potions, long success) 
    {
        Array.Sort(potions);
        List<int> result = new List<int>();
        int m = potions.Length;
        foreach (int spell in spells)
        {
            if (success % Convert.ToInt64(spell) == 0)
            {
                result.Add(m - bisectLeft(potions, success / Convert.ToInt64(spell)));
            }
            else
            {
                result.Add(m - bisectRight(potions, success / Convert.ToInt64(spell)));
            }
        }
        return result.ToArray();
    }
}
// @lc code=end
