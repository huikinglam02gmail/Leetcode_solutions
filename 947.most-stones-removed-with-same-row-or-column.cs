/*
 * @lc app=leetcode id=947 lang=csharp
 *
 * [947] Most Stones Removed with Same Row or Column
 */

// @lc code=start
public class Solution 
{
    public int RemoveStones(int[][] stones) 
    {
        Dictionary<int, List<int>>[] hashTable = new Dictionary<int, List<int>>[2];
        int n = stones.Length;
        int result = 0;
        bool[] visited = new bool[n];
        HashSet<int>[] graph = new HashSet<int>[n];
        Queue<int> queue = new Queue<int>();
        HashSet<int> seen = new HashSet<int>();

        for (int j = 0; j < 2; j++)
        {
            hashTable[j] = new Dictionary<int, List<int>>();
            for (int i = 0; i < n; i++)
            {
                if (!hashTable[j].ContainsKey(stones[i][j]))
                {
                    hashTable[j][stones[i][j]] = new List<int>();
                }
                hashTable[j][stones[i][j]].Add(i);
            }
        }

        for (int i = 0; i < n; i++)
        {
            graph[i] = new HashSet<int>();
        }

        for (int x = 0; x < 2; x++)
        {
            foreach (KeyValuePair<int, List<int>> kvp in hashTable[x])
            {
                int l = kvp.Value.Count;
                for (int i = 0; i < l - 1; i++)
                {
                    for (int j = i + 1; j < l; j++)
                    {
                        graph[kvp.Value[i]].Add(kvp.Value[j]);
                        graph[kvp.Value[j]].Add(kvp.Value[i]);
                    }
                }
            }
        }

        Array.Fill(visited, false);
        for (int i = 0; i < n; i++)
        {
            if (!visited[i])
            {
                queue.Clear();
                seen.Clear();
                queue.Enqueue(i);
                visited[i] = true;
                seen.Add(i);

                while (queue.Count > 0)
                {
                    int node = queue.Dequeue();
                    foreach (int nxt in graph[node])
                    {
                        if (!visited[nxt])
                        {
                            queue.Enqueue(nxt);
                            seen.Add(nxt);
                            visited[nxt] = true;
                        }
                    }
                }
                result += seen.Count - 1;
            }
        }
        return result;       
    }
}
// @lc code=end

