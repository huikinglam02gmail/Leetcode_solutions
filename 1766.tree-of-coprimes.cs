/*
 * @lc app=leetcode id=1766 lang=csharp
 *
 * [1766] Tree of Coprimes
 */

// @lc code=start
using System;
using System.Collections.Generic;

public class Solution
{
    public int[] GetCoprimes(int[] nums, int[][] edges)
    {
        var coPrimes = new HashSet<int>[51];
        coPrimes = coPrimes.Select(x => new HashSet<int>()).ToArray();
        for (int i = 1; i <= 50; i++)
        {
            for (int j = i; j <= 50; j++)
            {
                if (Gcd(i, j) == 1)
                {
                    coPrimes[i].Add(j);
                    coPrimes[j].Add(i);
                }
            }
        }

        var graph = new HashSet<int>[nums.Length];
        graph = graph.Select(x => new HashSet<int>()).ToArray();
        foreach (var edge in edges)
        {
            int a = edge[0];
            int b = edge[1];
            graph[a].Add(b);
            graph[b].Add(a);
        }

        var result = new int[nums.Length];
        Array.Fill(result, -1);
        var numseen = new Dictionary<int, List<int[]>>();
        var onpath = new HashSet<int>();

        void DFS(int node, int steps)
        {
            int lastIndex = -1;
            int minDist = int.MaxValue;
            foreach (int cop in coPrimes[nums[node]])
            {
                if (numseen.ContainsKey(cop) && numseen[cop].Count > 0 && (steps - numseen[cop][^1][1]) < minDist)
                {
                    minDist = steps - numseen[cop][^1][1];
                    lastIndex = numseen[cop][^1][0];
                }
            }

            result[node] = lastIndex;
            onpath.Add(node);

            if (!numseen.ContainsKey(nums[node]))
            {
                numseen[nums[node]] = new List<int[]>();
            }

            numseen[nums[node]].Add(new int[] { node, steps });

            foreach (int nxt in graph[node])
            {
                if (!onpath.Contains(nxt))
                {
                    DFS(nxt, steps + 1);
                }
            }

            onpath.Remove(node);
            numseen[nums[node]].RemoveAt(numseen[nums[node]].Count - 1);
        }

        DFS(0, 0);
        return result;
    }

    private int Gcd(int a, int b)
    {
        while (b != 0)
        {
            int temp = b;
            b = a % b;
            a = temp;
        }
        return a;
    }
}

// @lc code=end

