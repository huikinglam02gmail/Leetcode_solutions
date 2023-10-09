/*
 * @lc app=leetcode id=1942 lang=csharp
 *
 * [1942] The Number of the Smallest Unoccupied Chair
 */

// @lc code=start
using System;
using System.Collections.Generic;

public class Solution {
    public int SmallestChair(int[][] times, int targetFriend) 
    {
        PriorityQueue<int, int> free = new PriorityQueue<int, int>();
        int curChair = -1;
        List<int[]> timesWithIndex = new List<int[]>();
        
        for (int i = 0; i < times.Length; i++) {
            int[] timeWithIndex = new int[3];
            timeWithIndex[0] = times[i][0];
            timeWithIndex[1] = times[i][1];
            timeWithIndex[2] = i;
            timesWithIndex.Add(timeWithIndex);
        }
        
        timesWithIndex.Sort((a, b) => a[0] - b[0]);
        PriorityQueue<int, int> occupied = new PriorityQueue<int, int>();
        
        foreach (var item in timesWithIndex) {
            int arrival = item[0];
            int leaving = item[1];
            int i = item[2];
            
            while (occupied.TryPeek(out int ind, out int l) && l <= arrival) 
            {
                occupied.Dequeue();
                free.Enqueue(ind, ind);
            }
            
            if (free.Count == 0) {
                curChair += 1;
                free.Enqueue(curChair, curChair);
            }
            
            int freeChairToUse = free.Dequeue();
            
            if (i == targetFriend) {
                return freeChairToUse;
            }
            
            occupied.Enqueue(freeChairToUse, leaving);
        }
        
        return -1;
    }
}

// @lc code=end

