/*
 * @lc app=leetcode id=2251 lang=csharp
 *
 * [2251] Number of Flowers in Full Bloom
 */

// @lc code=start
using System;
using System.Collections.Generic;

public class Solution {
    public int[] FullBloomFlowers(int[][] flowers, int[] people) {
        List<int[]> peopleByArrival = new List<int[]>();
        for (int i = 0; i < people.Length; i++) {
            peopleByArrival.Add(new int[] { people[i], i });
        }
        peopleByArrival.Sort((a, b) => a[0] - b[0]);

        Array.Sort(flowers, (a, b) => a[0] - b[0]);

        PriorityQueue<int, int> endHeap = new PriorityQueue<int, int>();
        int[] result = new int[people.Length];
        Array.Fill(result, 0);
        int flowerPtr = 0;

        for (int i = 0; i < people.Length; i++) {
            int time = peopleByArrival[i][0];
            int index = peopleByArrival[i][1];

            while (flowerPtr < flowers.Length && flowers[flowerPtr][0] <= time) {
                endHeap.Enqueue(flowers[flowerPtr][1], flowers[flowerPtr][1]);
                flowerPtr++;
            }

            while (endHeap.Count > 0 && endHeap.Peek() < time) {
                endHeap.Dequeue();
            }

            result[index] = endHeap.Count;
        }

        return result;
    }
}

// @lc code=end

