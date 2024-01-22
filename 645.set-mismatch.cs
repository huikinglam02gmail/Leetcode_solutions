/*
 * @lc app=leetcode id=645 lang=csharp
 *
 * [645] Set Mismatch
 */

// @lc code=start
using System;
using System.Collections.Generic;

public class Solution
{
    public int[] FindErrorNums(int[] nums)
    {
        HashSet<int> hashSet = new HashSet<int>();
        int n = nums.Length;
        List<int> result = new List<int>();
        int total = 0;

        foreach (int num in nums)
        {
            if (!hashSet.Contains(num))
            {
                hashSet.Add(num);
                total += num;
            }
            else
            {
                result.Add(num);
            }
        }

        result.Add(n * (n + 1) / 2 - total);
        return result.ToArray();
    }
}

// @lc code=end

