/*
 * @lc app=leetcode id=839 lang=csharp
 *
 * [839] Similar String Groups
 */

// @lc code=start
using System.Collections.Generic;
public class Solution 
{
    public bool similar(string s1, string s2)
    {
        int count = 0;
        for (int i = 0; i < s1.Length; i++)
        {
            if (s1[i] != s2[i])
            {
                count++;
            }
            if (count > 2)
            {
                return false;
            }
        }
        return count == 2;
    }

    public int NumSimilarGroups(string[] strs) 
    {
        int n = strs.Length;
        Dictionary<string, HashSet<string>> graph = new Dictionary<string, HashSet<string>>();
        foreach(string s in strs)
        {
            if (!graph.ContainsKey(s))
            {
                graph.Add(s, new HashSet<string>());                
            }
        }
        for (int i = 0; i < n - 1; i++)
        {
            for (int j = i + 1; j < n; j++)
            {
                if (similar(strs[i], strs[j]))
                {
                    graph[strs[i]].Add(strs[j]);
                    graph[strs[j]].Add(strs[i]);
                }
            }
        }

        HashSet<string> visited = new HashSet<string>();
        Queue<string> queue = new Queue<string>();
        int count = 0;
        foreach(string s in strs)
        {
            if (!visited.Contains(s))
            {
                count++;
                queue.Clear();
                queue.Enqueue(s);
                visited.Add(s);
                while (queue.TryDequeue(out string node))
                {
                    foreach (string nxt in graph[node])
                    {
                        if (!visited.Contains(nxt))
                        {
                            queue.Enqueue(nxt);
                            visited.Add(nxt);
                        }
                    }
                }
            }
        }
        return count;
    }
}
// @lc code=end

