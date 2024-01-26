/*
 * @lc app=leetcode id=2605 lang=csharp
 *
 * [2605] Form Smallest Number From Two Digit Arrays
 */

// @lc code=start
using System;
using System.Collections.Generic;

public class Solution
{
    /**
     * Brute force
     */
    public int MinNumber(int[] nums1, int[] nums2)
    {
        for (int i = 1; i < 100; i++)
        {
            if (i < 10 && nums1.Contains(i) && nums2.Contains(i))
                return i;
            else
            {
                int i1 = i / 10;
                int i2 = i % 10;
                if ((nums1.Contains(i1) && nums2.Contains(i2)) || (nums1.Contains(i2) && nums2.Contains(i1)))
                    return i;
            }
        }
        return -1;
    }
}

// @lc code=end

