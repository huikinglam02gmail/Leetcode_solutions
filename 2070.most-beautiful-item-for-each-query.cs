/*
 * @lc app=leetcode id=2070 lang=csharp
 *
 * [2070] Most Beautiful Item for Each Query
 */

// @lc code=start
using System;
using System.Collections.Generic;
using System.Linq;

public class Solution {
    public int[] MaximumBeauty(int[][] items, int[] queries) {
        var Q = queries.Select((q, i) => new { Query = q, Index = i }).ToList();
        Q.Sort((a, b) => a.Query.CompareTo(b.Query));
        Array.Sort(items, (a, b) => {
            if (a[0] != b[0]) return a[0].CompareTo(b[0]);
            return a[1].CompareTo(b[1]);
        });
        
        int[] result = new int[queries.Length];
        int iQ = 0, iItem = 0;
        int maxSoFar = 0;
        for (int i = 0; i < Q.Count; i++) {
            while (iItem < items.Length && items[iItem][0] <= Q[i].Query) {
                maxSoFar = Math.Max(maxSoFar, items[iItem][1]);
                iItem++;
            }
            result[Q[i].Index] = maxSoFar;
        }
        return result;
    }
}

// @lc code=end

