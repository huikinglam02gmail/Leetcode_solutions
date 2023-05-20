/*
 * @lc app=leetcode id=399 lang=csharp
 *
 * [399] Evaluate Division
 */

// @lc code=start
using System.Collections.Generic;
using System;
using System.Linq;
public class Solution 
{
    public double[] CalcEquation(IList<IList<string>> equations, double[] values, IList<IList<string>> queries) 
    {
        Dictionary<string, HashSet<Tuple<string, double>>> graph = new Dictionary<string, HashSet<Tuple<string, double>>>();
        for (int i = 0; i < equations.Count; i++)
        {
            if (!graph.ContainsKey(equations[i][0]))
            {
                graph[equations[i][0]] = new HashSet<Tuple<string, double>>();
            }
            if (!graph.ContainsKey(equations[i][1]))
            {
                graph[equations[i][1]] = new HashSet<Tuple<string, double>>();
            }
            graph[equations[i][0]].Add(new Tuple<string, double>(equations[i][1], values[i]));
            graph[equations[i][1]].Add(new Tuple<string, double>(equations[i][0], 1d / values[i]));
        }

        List<double> result = new List<double>();
        Queue<Tuple<string, double>> queue = new Queue<Tuple<string, double>>();
        HashSet<string> visited = new HashSet<string>();
        for (int i = 0; i < queries.Count; i++)
        {
            if (graph.ContainsKey(queries[i][0]) && graph.ContainsKey(queries[i][1]))
            {
                queue.Clear();
                visited.Clear();
                queue.Enqueue(new Tuple<string, double>(queries[i][0], 1));
                visited.Add(queries[i][0]);
                while (queue.TryDequeue(out Tuple<string, double> t))
                {
                    if (t.Item1 == queries[i][1])
                    {
                        result.Add(t.Item2);
                        break;
                    }
                    foreach (Tuple<string, double> t2 in graph[t.Item1])
                    {
                        if (!visited.Contains(t2.Item1))
                        {
                            visited.Add(t2.Item1);
                            queue.Enqueue(new Tuple<string, double>(t2.Item1, t.Item2 * t2.Item2));
                        }
                    }
                }
            }
            if (result.Count < i + 1)
            {
                result.Add(-1);
            }
        }
        return result.ToArray();
    }
}
// @lc code=end

