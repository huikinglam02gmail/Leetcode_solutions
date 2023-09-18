/*
 * @lc app=leetcode id=1337 lang=csharp
 *
 * [1337] The K Weakest Rows in a Matrix
 */

// @lc code=start
using System;
using System.Collections.Generic;
using System.Linq;

public class Solution {
    public int[] KWeakestRows(int[][] mat, int k) {
        return (from row in mat.Select((value, index) => new { Index = index, Sum = value.Sum() })
                orderby row.Sum, row.Index
                select row.Index).Take(k).ToArray();
    }
}

// @lc code=end

