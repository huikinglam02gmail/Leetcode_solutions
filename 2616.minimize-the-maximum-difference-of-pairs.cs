/*
 * @lc app=leetcode id=2616 lang=csharp
 *
 * [2616] Minimize the Maximum Difference of Pairs
 */

// @lc code=start
using System;
using System.Collections.Generic;

public class Solution
{
    public bool CanForm(int p, int diff)
    {
        int pairs = 0;
        int i = 0;
        while (i < nums.Length - 1)
        {
            if (nums[i + 1] - nums[i] <= diff)
            {
                pairs++;
                i += 2;
            }
            else
            {
                i++;
            }
        }
        return pairs >= p;
    }

    public int MinimizeMax(int[] nums, int p)
    {
        Array.Sort(nums);
        this.nums = nums;
        int l = 0, r = nums[^1] - nums[0];
        while (l < r)
        {
            int mid = l + (r - l) / 2;
            if (CanForm(p, mid))
            {
                r = mid;
            }
            else
            {
                l = mid + 1;
            }
        }
        return l;
    }

    private int[] nums;
}

// @lc code=end

