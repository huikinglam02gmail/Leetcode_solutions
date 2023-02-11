/*
 * @lc app=leetcode id=1129 lang=csharp
 *
 * [1129] Shortest Path with Alternating Colors
 */

// @lc code=start
public class Solution 
{
    public int[] ShortestAlternatingPaths(int n, int[][] redEdges, int[][] blueEdges) 
    {
        Dictionary<Tuple<int, int>, HashSet<Tuple<int, int>>> graph = new Dictionary<Tuple<int, int>, HashSet<Tuple<int, int>>>();
        Queue<Tuple<int, int>> queue = new Queue<Tuple<int, int>>();
        HashSet<Tuple<int, int>> visited = new HashSet<Tuple<int, int>>();
        int steps = 0;
        graph.Add(new Tuple<int, int>(0, 0), new HashSet<Tuple<int, int>>());
        graph.Add(new Tuple<int, int>(0, 1), new HashSet<Tuple<int, int>>());
        foreach (int[] redEdge in redEdges)
        {
            Tuple<int, int> t = new Tuple<int, int>(redEdge[0], 1);
            if (!graph.ContainsKey(t))
            {
                graph.Add(t, new HashSet<Tuple<int, int>>());
            }
            graph[t].Add(new Tuple<int, int>(redEdge[1], 0));
        }
        foreach (int[] blueEdge in blueEdges)
        {
            Tuple<int, int> t = new Tuple<int, int>(blueEdge[0], 0);
            if (!graph.ContainsKey(t))
            {
                graph.Add(t, new HashSet<Tuple<int, int>>());
            }
            graph[t].Add(new Tuple<int, int>(blueEdge[1], 1));
        }
        
        int[] result = new int[n];
        Array.Fill(result, Int32.MaxValue);
        queue.Enqueue(new Tuple<int, int>(0, 0));
        queue.Enqueue(new Tuple<int, int>(0, 1));
        while (queue.Count > 0)
        {
            int l = queue.Count;
            for (int i = 0; i < l; i++)
            {
                Tuple<int, int> t = queue.Dequeue();
                result[t.Item1] = Math.Min(result[t.Item1], steps);
                if (graph.ContainsKey(t))
                {
                    foreach (Tuple<int, int> nxt in graph[t])
                    {
                        if (!visited.Contains(nxt))
                        {
                            queue.Enqueue(nxt);
                            visited.Add(nxt);
                        }
                    }
                }               
            }
            steps++;
        }
        for (int i = 0; i < n; i++)
        {
            if (result[i] == Int32.MaxValue)
            {
                result[i] = -1;
            }
        }
        return result;
    }
}
// @lc code=end

