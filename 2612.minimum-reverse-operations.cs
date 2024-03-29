/*
 * @lc app=leetcode id=2612 lang=csharp
 *
 * [2612] Minimum Reverse Operations
 */

// @lc code=start
using System;
using System.Collections.Generic;
using System.Linq;
public class Solution 
{
    public int[] MinReverseOperations(int n, int p, int[] banned, int k) 
    {
        int[] result = new int[n];
        Array.Fill(result, -1);

        SortedSet<int>[] trees = new SortedSet<int>[2];
        trees = trees.Select(x => new SortedSet<int>()).ToArray();
        HashSet<int> bannedSet = new HashSet<int>(banned);

        for (int i = 0; i < n; i++)
        {
            if (!bannedSet.Contains(i))
            {
                trees[i % 2].Add(i);
            }
        }

        Queue<int[]> queue = new Queue<int[]>();
        queue.Enqueue(new int[2]{p, 0});
        trees[p % 2].Remove(p);
        while (queue.TryDequeue(out int[] item))
        {
            result[item[0]] = item[1];
            int[] nodesToRemove = trees[Math.Abs(k - 1 - item[0]) % 2].GetViewBetween(2*Math.Max(0, item[0] - k + 1) + k - 1 - item[0], 2*Math.Min(item[0] + 1, n + 1 - k) + k - 3 - item[0]).ToArray();
            foreach (int node in nodesToRemove)
            {
                trees[Math.Abs(k - 1 - item[0]) % 2].Remove(node);
                queue.Enqueue(new int[2]{node, item[1] + 1});
            }
        }
        return result;
    }
}
// @lc code=end
