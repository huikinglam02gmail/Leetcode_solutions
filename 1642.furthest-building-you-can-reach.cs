/*
 * @lc app=leetcode id=1642 lang=csharp
 *
 * [1642] Furthest Building You Can Reach
 */

// @lc code=start
using System;
using System.Collections.Generic;

public class Solution {
    public int FurthestBuilding(int[] heights, int bricks, int ladders) {
        PriorityQueue<int, int> heap = new PriorityQueue<int, int>(); // Custom priority queue implementation
        int result = 0;
        
        for (int i = 0; i < heights.Length - 1; i++) {
            if (heights[i + 1] > heights[i]) {
                heap.Enqueue(heights[i + 1] - heights[i], heights[i + 1] - heights[i]);
                
                if (ladders < heap.Count && heap.TryDequeue(out int use, out int priority)) {
                    bricks -= use;
                    if (bricks < 0) {
                        return i;
                    }
                }
            }
            result = i + 1;
        }
        
        return result;
    }
}

// @lc code=end

