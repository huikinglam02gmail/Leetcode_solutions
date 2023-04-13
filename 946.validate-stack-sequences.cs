/*
 * @lc app=leetcode id=946 lang=csharp
 *
 * [946] Validate Stack Sequences
 */

// @lc code=start
using System.Collections.Generic;
public class Solution 
{
    public bool ValidateStackSequences(int[] pushed, int[] popped) 
    {
        Stack<int> stack = new Stack<int>();
        int n = pushed.Length;
        int j = 0;
        foreach (int num in pushed)
        {
            if (num != popped[j])
            {
                stack.Push(num);
            }
            else
            {
                j++;
                while (stack.Count > 0 && stack.Peek() == popped[j])
                {
                    stack.Pop();
                    j++;
                }
            }
        }
        return j == n;
    }
}
// @lc code=end

