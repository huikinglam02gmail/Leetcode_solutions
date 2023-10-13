/*
 * @lc app=leetcode id=1943 lang=csharp
 *
 * [1943] Describe the Painting
 */

// @lc code=start
/**
 * @lc app=leetcode id=1943 lang=csharp
 *
 * [1943] Describe the Painting
 */

using System;
using System.Collections.Generic;

public class Solution {
    private void EndOldSegment(long i, long totalColor) {
        if (result.Count > 0) {
            result.Last()[1] = i;
            result.Last()[2] = totalColor;
        }
    }

    private void AddNewSegment(long i) {
        result.Add(new List<long> { i, -1, -1 });
    }

private List<IList<long>> result;
    public IList<IList<long>> SplitPainting(int[][] segments) {
        PriorityQueue<int, int> exit = new PriorityQueue<int, int>();
        result = new List<IList<long>>();
        long cumu = 0;
        int segmentPtr = 0;

        segments = segments.OrderBy(x => x[0]).ToArray();

        int limit = 0;
        foreach (var segment in segments) {
            limit = Math.Max(limit, segment[1]);
        }

        for (int i = 1; i <= limit; i++) {
            int countSameEnd = 0;
            while (exit.TryPeek(out int color, out int end) && end == i) 
            {
                exit.Dequeue();
                countSameEnd++;

                if (countSameEnd == 1) {
                    EndOldSegment(i, cumu);
                    AddNewSegment(i);
                }

                cumu -= color;
            }

            int countSameStart = 0;
            while (segmentPtr < segments.Length && segments[segmentPtr][0] == i) 
            {
                var segment = segments[segmentPtr];
                exit.Enqueue(segment[2], segment[1]);
                countSameStart++;

                if (countSameStart == 1) 
                {
                    if (cumu > 0 && result.Count > 0 && result.Last()[0] != i) 
                    {
                        EndOldSegment(i, cumu);
                        AddNewSegment(i);
                    } 
                    else if (result.Count > 0) 
                    {
                        result.Last()[0] = i;
                    } 
                    else 
                    {
                        AddNewSegment(i);
                    }
                }
                cumu += segment[2];
                segmentPtr++;
            }
        }

        result.RemoveAt(result.Count - 1);

        return result;
    }
}

// @lc code=end

