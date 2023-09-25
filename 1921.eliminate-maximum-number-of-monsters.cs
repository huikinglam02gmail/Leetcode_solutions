/*
 * @lc app=leetcode id=1921 lang=csharp
 *
 * [1921] Eliminate Maximum Number of Monsters
 */

// @lc code=start
using System;
using System.Collections.Generic;

public class Solution {
    public int EliminateMaximum(int[] dist, int[] speed) 
    {
        PriorityQueue<int, double> minHeap = new PriorityQueue<int, double>();
        int n = dist.Length;
        
        for (int i = 0; i < n; i++) 
        {
            minHeap.Enqueue(i, (double)dist[i] / (double)speed[i]);
        }

        int result = 0;
        while (minHeap.TryDequeue(out int i, out double time) && time > result) {
            result++;
        }
        
        return result;
    }
}
// @lc code=end

