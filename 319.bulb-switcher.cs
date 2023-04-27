/*
 * @lc app=leetcode id=319 lang=csharp
 *
 * [319] Bulb Switcher
 */

// @lc code=start
using System;
public class Solution 
{
    public int BulbSwitch(int n) 
    {
        return Convert.ToInt32(Math.Floor(Math.Sqrt(n)));
    }
}
// @lc code=end

