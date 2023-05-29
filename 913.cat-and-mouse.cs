/*
 * @lc app=leetcode id=913 lang=csharp
 *
 * [913] Cat and Mouse
 */

// @lc code=start
using System.Collections.Generic;

public class Solution
{
    public int CatMouseGame(int[][] graph)
    {
        int n = graph.Length;

        int[][][] degree = new int[n][][];
        for (int i = 0; i < n; i++)
        {
            degree[i] = new int[n][];
            for (int j = 0; j < n; j++)
            {
                degree[i][j] = new int[3];
            }
        }

        for (int i = 0; i < n; i++)
        {
            for (int j = 0; j < n; j++)
            {
                degree[i][j][1] += graph[i].Length;
                degree[i][j][2] += graph[j].Length;
                if (Array.IndexOf(graph[j], 0) >= 0)
                {
                    degree[i][j][2] -= 1;
                }
            }
        }

        Queue<int[]> dq = new Queue<int[]>();
        int[][][] win = new int[n][][];
        for (int i = 0; i < n; i++)
        {
            win[i] = new int[n][];
            for (int j = 0; j < n; j++)
            {
                win[i][j] = new int[3];
            }
        }

        for (int i = 1; i < n; i++)
        {
            for (int k = 1; k <= 2; k++)
            {
                win[0][i][k] = 1;
                dq.Enqueue(new int[] { 0, i, k, 1 });
                win[i][i][k] = 2;
                dq.Enqueue(new int[] { i, i, k, 2 });
            }
        }

        while (dq.Count > 0)
        {
            int[] state = dq.Dequeue();
            int m = state[0];
            int c = state[1];
            int t = state[2];
            int w = state[3];

            List<int[]> parents = new List<int[]>();
            if (t == 1)
            {
                foreach (int parent in graph[c])
                {
                    if (parent != 0)
                    {
                        parents.Add(new int[] { m, parent, 2 });
                    }
                }
            }
            else
            {
                foreach (int parent in graph[m])
                {
                    parents.Add(new int[] { parent, c, 1 });
                }
            }

            foreach (int[] parentState in parents)
            {
                int mp = parentState[0];
                int cp = parentState[1];
                int tp = parentState[2];

                if (win[mp][cp][tp] == 0)
                {
                    if (tp == w)
                    {
                        win[mp][cp][tp] = w;
                        dq.Enqueue(new int[] { mp, cp, tp, w });
                    }
                    else
                    {
                        degree[mp][cp][tp] -= 1;
                        if (degree[mp][cp][tp] == 0)
                        {
                            win[mp][cp][tp] = w;
                            dq.Enqueue(new int[] { mp, cp, tp, w });
                        }
                    }
                }
            }
        }

        return win[1][2][1];
    }
}

// @lc code=end

