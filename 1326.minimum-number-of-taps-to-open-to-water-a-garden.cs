/*
 * @lc app=leetcode id=1326 lang=csharp
 *
 * [1326] Minimum Number of Taps to Open to Water a Garden
 */

// @lc code=start
using System;
using System.Collections.Generic;

public class Solution
{
    public int MinTaps(int n, int[] ranges)
    {
        var heap = new PriorityQueue<int, int>();
        var candidates = new List<int[]>();
        for (int i = 0; i < ranges.Length; i++)
        {
            candidates.Add(new int[] { i - ranges[i], i + ranges[i] });
        }
        candidates = candidates.OrderBy(x => x[0]).ThenBy(x => x[1]).ToList();
        int result = 0, cur = 0, ind = 0;
        while (cur < n)
        {
            while (ind < candidates.Count && cur >= candidates[ind][0])
            {
                heap.Enqueue(candidates[ind][1], - candidates[ind][1]);
                ind++;
            }
            if (heap.Count > 0 && heap.Peek() > cur)
            {
                cur = heap.Dequeue();
                result++;
            }
            else
            {
                return -1;
            }
        }
        return result;
    }
}
// @lc code=end

