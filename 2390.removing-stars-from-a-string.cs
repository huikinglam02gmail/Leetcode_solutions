/*
 * @lc app=leetcode id=2390 lang=csharp
 *
 * [2390] Removing Stars From a String
 */

// @lc code=start
using System.Collections.Generic;
public class Solution 
{
    public string RemoveStars(string s) 
    {
        List<char> stack = new List<char>();
        foreach (char c in s)
        {
            if (c == '*')
            {
                if (stack.Count > 0)
                {
                    stack.RemoveAt(stack.Count - 1);
                }
            }
            else
            {
                stack.Add(c);
            }
        }
        return string.Join("", stack);
    }
}
// @lc code=end

