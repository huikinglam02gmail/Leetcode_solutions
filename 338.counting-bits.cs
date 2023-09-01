/*
 * @lc app=leetcode id=338 lang=csharp
 *
 * [338] Counting Bits
 */

// @lc code=start
using System;
using System.Collections.Generic;

public class Solution
{
    public int[] CountBits(int n)
    {
        int cur = -1;
        List<int> result = new List<int> { 0 };
        
        for (int i = 1; i <= n; i++)
        {
            while (i >= (1 << (cur + 1)))
            {
                cur++;
            }
            result.Add(result[i - (1 << cur)] + 1);           
        }
        
        return result.ToArray();
    }
}

// @lc code=end

