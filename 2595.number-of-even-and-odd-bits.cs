/*
 * @lc app=leetcode id=2595 lang=csharp
 *
 * [2595] Number of Even and Odd Bits
 */

// @lc code=start
using System;
using System.Collections.Generic;

public class Solution
{
    /**
     * Just do as described
     */
    public int[] EvenOddBit(int n)
    {
        string nString = Convert.ToString(n, 2);
        int[] result = { 0, 0 };
        for (int i = nString.Length - 1; i >= 0; --i) if (nString[i] == '1') result[(nString.Length - 1 - i) % 2]++;

        return result;
    }
}

// @lc code=end

