/*
 * @lc app=leetcode id=646 lang=csharp
 *
 * [646] Maximum Length of Pair Chain
 */

// @lc code=start
using System;
using System.Linq;

public class Solution {
    public int FindLongestChain(int[][] pairs) {
        Array.Sort(pairs, (x, y) => x[1].CompareTo(y[1]));
        List<int> chain = new List<int>();
        
        foreach (var pair in pairs) {
            if (chain.Count == 0 || pair[0] > chain.Last()) {
                chain.Add(pair[1]);
            }
        }
        
        return chain.Count;
    }
}

// @lc code=end

