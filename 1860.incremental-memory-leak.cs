/*
 * @lc app=leetcode id=1860 lang=csharp
 *
 * [1860] Incremental Memory Leak
 */

// @lc code=start
using System;
using System.Collections.Generic;

public class Solution
{
    public int[] MemLeak(int memory1, int memory2)
    {
        var heap = new PriorityQueue<int, Tuple<int, int>>();
        heap.Enqueue(0, new Tuple<int, int>(- memory1, 0));
        heap.Enqueue(1, new Tuple<int, int>(- memory2, 1));
        int i = 1;
        while (heap.TryPeek(out int element, out Tuple<int, int> priority) && priority.Item1 <= - i)
        {
            var ele = heap.Dequeue();
            heap.Enqueue(element, new Tuple<int, int>(i + priority.Item1, element));
            i++;
        }
        int[] result = new int[3];
        result[0] = i;
        while (heap.TryDequeue(out int element, out Tuple<int, int> priority))
        {
            result[element + 1] = - priority.Item1;
        }
        return result;
    }
}

// @lc code=end

