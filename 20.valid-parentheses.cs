/*
 * @lc app=leetcode id=20 lang=csharp
 *
 * [20] Valid Parentheses
 */

// @lc code=start
using System.Collections.Generic;
public class Solution 
{
    Dictionary<char, char> pairs = new Dictionary<char, char>(){ { '(',')'}, { '[',']'}, { '{','}'}};
    public bool IsValid(string s) 
    {
        Stack<char> stack = new Stack<char>();
        foreach (char c in s)
        {
            if (pairs.ContainsKey(c))
            {
                stack.Push(c);
            }
            else if (stack.Count > 0)
            {
                if (c == pairs[stack.Peek()])
                {
                    stack.Pop();
                }
                else
                {
                    return false;
                }
            }
            else
            {
                return false;
            }
        }
        return stack.Count == 0;
    }
}
// @lc code=end

