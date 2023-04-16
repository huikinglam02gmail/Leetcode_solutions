/*
 * @lc app=leetcode id=2646 lang=csharp
 *
 * [2646] Minimize the Total Price of the Trips
 */

// @lc code=start
using System.Collections.Generic;
using System.Linq;
using System;
public class Solution 
{
    int[] Price;
    int[] frequency;
    HashSet<int>[] graph;
    Dictionary<Tuple<int, bool>, int> memo = new Dictionary<Tuple<int, bool>, int>();

    public int dfs(int node, int parent, bool halfThisNode)
    {
        Tuple<int, bool> t = new Tuple<int, bool>(node, halfThisNode);
        if (memo.ContainsKey(t))
        {
            return memo[t];
        }
        else
        {
            int result = Price[node] * frequency[node];
            if (halfThisNode)
            {
                result /= 2;
            }
            foreach (int nxt in graph[node])
            {
                if (nxt != parent)
                {
                    int nxtNodeNotFlip = dfs(nxt, node, false);
                    int nxtNodeFlip = dfs(nxt, node, true);
                    if (halfThisNode)
                    {
                        result += nxtNodeNotFlip;
                    }
                    else
                    {
                        result += Math.Min(nxtNodeNotFlip, nxtNodeFlip);
                    }
                }
            }
            memo.Add(t, result);
            return result;
        }
    }

    public int MinimumTotalPrice(int n, int[][] edges, int[] price, int[][] trips) 
    {
        graph = new HashSet<int>[n];
        graph = graph.Select(x => new HashSet<int>()).ToArray();
        foreach (int[] edge in edges)
        {
            graph[edge[0]].Add(edge[1]);
            graph[edge[1]].Add(edge[0]);            
        }

        Price = price;
        frequency = new int[n];
        Array.Fill(frequency, 0);

        Queue<List<int>> queue = new Queue<List<int>>();
        HashSet<int> visited = new HashSet<int>();        
        foreach (int[] trip in trips)
        {
            queue.Clear();
            visited.Clear();
            queue.Enqueue(new List<int>(){trip[0]});
            visited.Add(trip[0]);

            while (queue.TryDequeue(out List<int> visitedNodes))
            {
                if (visitedNodes.Last() == trip[1])
                {
                    foreach (int visitedNode in visitedNodes)
                    {
                        frequency[visitedNode]++;
                    }
                    break;
                }
                foreach (int nxt in graph[visitedNodes.Last()])
                {
                    if (!visited.Contains(nxt))
                    {
                        queue.Enqueue(visitedNodes.Select(x => x).Append(nxt).ToList());
                        visited.Add(nxt);
                    }
                }
            }
        }
        return Math.Min(dfs(0, -1, true), dfs(0, -1, false));
    }
}
// @lc code=end

