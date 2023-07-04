/*
 * @lc app=leetcode id=137 lang=csharp
 *
 * [137] Single Number II
 */

// @lc code=start
using System.Collections.Generic;

public class Solution
{
    public int SingleNumber(int[] nums)
    {
        int ones = 0;
        int twos = 0;
        
        foreach (int num in nums)
        {
            ones = (ones ^ num) & ~twos;
            twos = (twos ^ num) & ~ones;
        }
        
        return ones;
    }
}

// @lc code=end

