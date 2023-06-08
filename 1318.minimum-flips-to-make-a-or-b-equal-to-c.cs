/*
 * @lc app=leetcode id=1318 lang=csharp
 *
 * [1318] Minimum Flips to Make a OR b Equal to c
 */

// @lc code=start
using System;
public class Solution {
    public int MinFlips(int a, int b, int c) {
        int result = 0;
        for (int i = 0; i < 32; i++) 
        {
            if ((c & (1 << i)) == 0) 
            {
                result += Convert.ToInt32((a & (1 << i)) != 0) + Convert.ToInt32((b & (1 << i)) != 0);
            }
            else 
            {
                result += Math.Max(1, Convert.ToInt32((a & (1 << i)) == 0) + Convert.ToInt32((b & (1 << i)) == 0)) - 1;
            }
        }
        return result;
    }
}

// @lc code=end

