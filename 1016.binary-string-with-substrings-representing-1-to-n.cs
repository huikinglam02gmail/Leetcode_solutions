/*
 * @lc app=leetcode id=1016 lang=csharp
 *
 * [1016] Binary String With Substrings Representing 1 To N
 */

// @lc code=start
using System;
public class Solution 
{
    public bool QueryString(string s, int n) 
    {
        for (int i = n; i > 0; i--)
        {
            if (!s.Contains(Convert.ToString(i, 2)))
            {
                return false;
            }
        }
        return true;
    }
}
// @lc code=end

