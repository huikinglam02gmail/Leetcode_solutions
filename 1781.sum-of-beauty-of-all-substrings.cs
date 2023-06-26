/*
 * @lc app=leetcode id=1781 lang=csharp
 *
 * [1781] Sum of Beauty of All Substrings
 */

// @lc code=start
using System;
using System.Linq;

public class Solution
{
    public int BeautySum(string s)
    {
        int result = 0;
        int n = s.Length;
        for (int i = 0; i < n; i++)
        {
            int[] count = new int[26];
            for (int j = i; j < n; j++)
            {
                count[s[j] - 'a']++;
                result += count.Max() - count.Where(c => c > 0).Min();
            }
        }
        return result;
    }
}

// @lc code=end

