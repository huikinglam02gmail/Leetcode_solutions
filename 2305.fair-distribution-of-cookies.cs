/*
 * @lc app=leetcode id=2305 lang=csharp
 *
 * [2305] Fair Distribution of Cookies
 */

// @lc code=start
using System;
using System.Collections.Generic;
using System.Linq;

public class Solution
{
    private int[] Cookies;
    private Dictionary<Tuple<int, string>, int> memo;

    private int DFS(int i, string stateString)
    {
        Tuple<int, string> tuple = new Tuple<int, string>(i, stateString);
        int[] state = stateString.Split("_").Select(x => Int32.Parse(x)).ToArray();
        if (i == Cookies.Length)
        {
            return state[state.Length - 1];
        }
        else if (!memo.ContainsKey(tuple))
        {
            int result = int.MaxValue;
            for (int j = 0; j < state.Length; j++)
            {
                state[j] += Cookies[i];
                result = Math.Min(result, DFS(i + 1, string.Join("_", state.OrderBy(x => x).Select(x => x.ToString()).ToArray())));
                state[j] -= Cookies[i];
            }
            memo.Add(tuple, result);
        }
        return memo[tuple];
    }

    public int DistributeCookies(int[] cookies, int k)
    {
        Cookies = cookies;
        memo = new Dictionary<Tuple<int, string>, int>();
        string[] initialState = new string[k];
        Array.Fill(initialState, "0");
        return DFS(0, string.Join("_", initialState));
    }
}

// @lc code=end

