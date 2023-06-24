/*
 * @lc app=leetcode id=956 lang=csharp
 *
 * [956] Tallest Billboard
 */

// @lc code=start
using System;
using System.Collections.Generic;

public class Solution
{
    private int[] rods;
    private Dictionary<string, int> cache;

    public int TallestBillboard(int[] rods)
    {
        this.rods = rods;
        this.cache = new Dictionary<string, int>();
        return DFS(0, 0);
    }

    private int DFS(int idx, int diff)
    {        
        if (idx == rods.Length)
        {
            return diff == 0 ? 0 : -10000;
        }
        string key = idx.ToString() + "-" + diff.ToString();
        if (!cache.ContainsKey(key))
        {
            int skip = DFS(idx + 1, diff);
            int longSupport = DFS(idx + 1, diff + rods[idx]);
            int shortSupport = diff >= rods[idx] ? DFS(idx + 1, diff - rods[idx]) + rods[idx] : DFS(idx + 1, rods[idx] - diff) + diff; 
            cache[key] = Math.Max(skip, Math.Max(longSupport, shortSupport));                     
        }
        return cache[key];
    }
}

// @lc code=end

