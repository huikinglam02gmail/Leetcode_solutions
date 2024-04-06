/*
 * @lc app=leetcode id=1249 lang=csharp
 *
 * [1249] Minimum Remove to Make Valid Parentheses
 */

// @lc code=start
using System.Collections.Generic;

public class Solution {
    /*
    Keep a stack to find if each parenthesis is valid
    In a stack, we keep the indices of open and close parenthesis [i, 1] or [i,-1]
    When a new parenthesis come in, we ask if it can close previous open parenthesis that results in a pop. The successful closes will be recorded as good parenthesis    
    */
    public string MinRemoveToMakeValid(string s) {
        var stack = new Stack<(int, int)>();
        var good = new HashSet<int>();
        
        for (int i = 0; i < s.Length; i++) {
            char c = s[i];
            if (c == '(') {
                stack.Push((i, 1));
            } else if (c == ')') {
                if (stack.Count > 0 && stack.Peek().Item2 == 1) {
                    var item = stack.Pop();
                    good.Add(item.Item1);
                    good.Add(i);
                } else {
                    stack.Push((i, -1));
                }
            }
        }

        StringBuilder result = new StringBuilder();
        for (int i = 0; i < s.Length; i++) {
            char c = s[i];
            if (char.IsLetter(c) || good.Contains(i)) {
                result.Append(c);
            }
        }
        
        return result.ToString();
    }
}

// @lc code=end

