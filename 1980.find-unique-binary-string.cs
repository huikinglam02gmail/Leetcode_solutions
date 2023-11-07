/*
 * @lc app=leetcode id=1980 lang=csharp
 *
 * [1980] Find Unique Binary String
 */

// @lc code=start
using System;
using System.Collections.Generic;

public class Solution
{
    public string FindDifferentBinaryString(string[] nums)
    {
        int n = nums.Length;
        int i = 0;
        while (i < (1 << n))
        {
            string binaryString = Convert.ToString(i, 2).PadLeft(n, '0');
            if (!Array.Exists(nums, element => element == binaryString))
            {
                return binaryString;
            }
            else
            {
                i++;
            }
        }
        return "";
    }
}

// @lc code=end

