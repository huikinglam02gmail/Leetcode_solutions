/*
 * @lc app=leetcode id=886 lang=csharp
 *
 * [886] Possible Bipartition
 */

// @lc code=start
using System;
using System.Collections;
public class Solution 
{
    public bool PossibleBipartition(int n, int[][] dislikes) 
    {
        HashSet<int>[] graph = new HashSet<int>[n];
        Queue<int> queue = new Queue<int>();
        for (int i = 0; i < n; i++)
        {
            graph[i] = new HashSet<int>();
        }
        foreach (int[] dislike in dislikes)
        {
            graph[dislike[0] - 1].Add(dislike[1] - 1);
            graph[dislike[1] - 1].Add(dislike[0] - 1);
        }

        HashSet<int> seen1 = new HashSet<int>();
        HashSet<int> seen2 = new HashSet<int>();

        for (int i = 0; i < n; i++)
        {
            if (!seen1.Contains(i) && !seen2.Contains(i))
            {
                queue.Clear();
                queue.Enqueue(i);
                seen1.Add(i);
                while (queue.TryDequeue(out int node))
                {
                    foreach (int nxt in graph[node])
                    {
                        if (seen1.Contains(node))
                        {
                            if (seen1.Contains(nxt))
                            {
                                return false;
                            }
                            if (!seen2.Contains(nxt))
                            {
                                seen2.Add(nxt);
                                queue.Enqueue(nxt);
                            }
                        }
                        else
                        {
                            if (seen2.Contains(nxt))
                            {
                                return false;
                            }
                            if (!seen1.Contains(nxt))
                            {
                                seen1.Add(nxt);
                                queue.Enqueue(nxt);
                            }
                        }
                    }
                }
            }
        }
        return true;
    }
}
// @lc code=end

