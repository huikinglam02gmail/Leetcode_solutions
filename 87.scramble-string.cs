/*
 * @lc app=leetcode id=87 lang=csharp
 *
 * [87] Scramble String
 */

// @lc code=start
using System.Collections.Generic;
using System;
public class Solution 
{
    Dictionary<Tuple<string, string>, bool> memo = new Dictionary<Tuple<string, string>, bool>();
    public bool IsScramble(string s1, string s2) 
    {
        Tuple<string, string> t = new Tuple<string, string>(s1, s2);
        if (memo.ContainsKey(t))
        {
            return memo[t];
        }
        else if (s1.Equals(s2))
        {
            memo[t] = true;
        }
        else
        {
            memo[t] = false;
            for (int i = 1; i < s1.Length; i++)
            {
                if ((IsScramble(s1.Substring(0, i), s2.Substring(0, i)) && IsScramble(s1.Substring(i), s2.Substring(i))) || (IsScramble(s1.Substring(s1.Length - i, i), s2.Substring(0, i)) && IsScramble(s1.Substring(0, s1.Length - i), s2.Substring(i))))
                {
                    memo[t] = true;
                }
            }
        }
        return memo[t];
    }
}
// @lc code=end

