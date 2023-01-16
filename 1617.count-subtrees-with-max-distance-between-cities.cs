/*
 * @lc app=leetcode id=1617 lang=csharp
 *
 * [1617] Count Subtrees With Max Distance Between Cities
 */

// @lc code=start
public class Solution 
{
    HashSet<int>[] graph;
    public List<int> bfs(int mask, int start)
    {
        Queue<int> queue = new Queue<int>();
        List<int> topoSort = new List<int>();
        HashSet<int> visited = new HashSet<int>();
        int steps = 0;

        queue.Enqueue(start);
        topoSort.Add(start);
        visited.Add(start);
        while (queue.Count > 0)
        {
            int n = queue.Count;
            for (int i = 0; i < n; i++)
            {
                int node = queue.Dequeue();
                foreach (int nxt in graph[node])
                {
                    if ((mask & (1 << nxt)) != 0 && !visited.Contains(nxt))
                    {
                        queue.Enqueue(nxt);
                        topoSort.Add(nxt);
                        visited.Add(nxt);
                    }
                }
            }
            if (queue.Count > 0)
            {
                steps++;
            }
        }
        topoSort.Add(steps);
        return topoSort;
    }

    public int setBitCounter(int mask)
    {
        int result = 0;
        while(mask > 0)
        {
            if (mask % 2 == 1)
            {
                result++;
            }
            mask >>= 1;
        }
        return result;
    }

    public int[] CountSubgraphsForEachDiameter(int n, int[][] edges) 
    {
        graph = new HashSet<int>[n];
        int[] result = new int[n];
        for (int i = 0; i < n; i++)
        {
            result[i] = 0;
            graph[i] = new HashSet<int>();
        }
        foreach (int[] edge in edges)
        {
            graph[edge[0] - 1].Add(edge[1] - 1);
            graph[edge[1] - 1].Add(edge[0] - 1);
        }

        for (int mask = 0; mask < (1 << n); mask++)
        {
            int i = 0;
            while (i < n && (mask & (1 << i)) == 0)
            {
                i++;
            }
            if (i < n)
            {
                List<int> bfsResult = bfs(mask, i);
                if (bfsResult.Count - 1 == setBitCounter(mask))
                {
                    List<int> bfsResultFromEdge = bfs(mask, bfsResult[bfsResult.Count - 2]);
                    result[bfsResultFromEdge[bfsResultFromEdge.Count - 1]]++;
                }
            }
        }
        return result[1..];
    }
}
// @lc code=end

