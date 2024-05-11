/*
 * @lc app=leetcode id=857 lang=csharp
 *
 * [857] Minimum Cost to Hire K Workers
 */

// @lc code=start
using System;
using System.Collections.Generic;
using System.Linq;

public class Solution {
    public double MincostToHireWorkers(int[] quality, int[] wage, int k) {
        var ratio = quality.Select((q, i) => new { Ratio = (double)wage[i] / q, Quality = q }).OrderBy(r => r.Ratio).ToArray();
        var heap = new PriorityQueue<int, int>();
        var qSum = 0;
        var result = double.PositiveInfinity;
        
        foreach (var worker in ratio) {
            qSum += worker.Quality;
            heap.Enqueue(worker.Quality, -worker.Quality);
            
            if (heap.Count > k && heap.TryDequeue(out int q, out int negQ))
                qSum -= q;
            
            if (heap.Count == k)
                result = Math.Min(result, qSum * worker.Ratio);
        }
        
        return result;
    }
}

// @lc code=end

