/*
 * @lc app=leetcode id=1851 lang=csharp
 *
 * [1851] Minimum Interval to Include Each Query
 */

// @lc code=start
using System;
using System.Collections.Generic;

public class Solution {
    public int[] MinInterval(int[][] intervals, int[] queries) {
        List<Tuple<int, int>> queriesWithIndex = new List<Tuple<int, int>>();
        for (int i = 0; i < queries.Length; i++) {
            queriesWithIndex.Add(new Tuple<int, int>(queries[i], i));
        }
        queriesWithIndex.Sort();

        intervals = intervals.OrderBy(x => x[0]).ThenBy(x => x[1]).ToArray();

        PriorityQueue<int, int> heap = new PriorityQueue<int, int>();
        int[] result = new int[queries.Length];
        Array.Fill(result, -1);
        int j = 0;
        for (int i = 0; i < queriesWithIndex.Count; i++) {
            int q = queriesWithIndex[i].Item1;
            int ind = queriesWithIndex[i].Item2;
            
            while (j < intervals.Length && intervals[j][0] <= q) {
                heap.Enqueue(intervals[j][1], intervals[j][1] - intervals[j][0] + 1);
                j++;
            }
            
            while (heap.TryPeek(out int e1, out int l1) && e1 < q) {
                heap.Dequeue();
            }

            if (heap.TryPeek(out int end, out int length))
            {
                result[ind] = length;
            }
        }       
        return result;
    }
}

// @lc code=end

