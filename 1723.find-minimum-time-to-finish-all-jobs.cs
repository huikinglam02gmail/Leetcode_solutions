/*
 * @lc app=leetcode id=1723 lang=csharp
 *
 * [1723] Find Minimum Time to Finish All Jobs
 */

// @lc code=start
using System.Collections.Generic;
using System;
using System.Linq;
public class Solution 
{
    Dictionary<Tuple<int, string>, int> cache = new Dictionary<Tuple<int, string>, int>();
    int[] Nums;
    int K;
    public int DFS(int i, string state)
    {
        Tuple<int, string> t = new Tuple<int, string>(i, state);
        int result;
        if (cache.ContainsKey(t))
        {
            return cache[t];
        }
        else if (i == Nums.Length)
        {
            result = state.Split('_').Select(s => Int32.Parse(s)).Max();                
        }
        else
        {
            int[] stateList = state.Split('_').Select(s => Int32.Parse(s)).ToArray();
            result = Int32.MaxValue;
            for (int l = 0; l < K; l++)
            {
                stateList[l] += Nums[i];
                if (stateList.Max() < result)
                {
                    result = Math.Min(result, DFS(i + 1, string.Join("_", stateList.OrderBy(j => j).Select(j => j.ToString()))));
                }
                stateList[l] -= Nums[i];
            }
        }
        cache.Add(t, result);
        return result;
    }

    public int MinimumTimeRequired(int[] jobs, int k) 
    {
        Nums = jobs.OrderByDescending(n => n).ToArray();
        K = k;
        return DFS(0, string.Join("_", Enumerable.Repeat("0", k)));            
    }
}
// @lc code=end

