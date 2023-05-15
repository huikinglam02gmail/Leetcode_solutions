/*
 * @lc app=leetcode id=1717 lang=csharp
 *
 * [1717] Maximum Score From Removing Substrings
 */

// @lc code=start
using System.Collections.Generic;
using System.Linq;
public class Solution 
{
    public int MaximumGain(string s, int x, int y) 
    {
        string[] order = x > y ? new string[2]{"ab","ba"} : new string[2] { "ba", "ab" };
        int[] score = x > y ? new int[2]{x,y} : new int[2] { y, x };
        List<char> stack1 = s.Select(c => c).ToList();
        List<char> stack2 = new List<char>();
        int result = 0;
        for (int i = 0; i < 2; i++)
        {
            foreach (char c in stack1)
            {
                if (stack2.Count > 0 && stack2.Last() == order[i][0] && c == order[i][1])
                {
                    stack2.RemoveAt(stack2.Count - 1);
                    result += score[i];
                }
                else
                {
                    stack2.Add(c);
                }
            }
            stack1 = stack2.Select(c => c).ToList();
            stack2.Clear();
        }
        return result;
    }
}
// @lc code=end

