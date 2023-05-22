/*
 * @lc app=leetcode id=1722 lang=csharp
 *
 * [1722] Minimize Hamming Distance After Swap Operations
 */

// @lc code=start
public class Solution 
{
    public int MinimumHammingDistance(int[] source, int[] target, int[][] allowedSwaps) 
    {
        List<HashSet<int>> graph = new List<HashSet<int>>();
        for (int i = 0; i < source.Length; i++)
        {
            graph.Add(new HashSet<int>());
        }

        foreach (var swap in allowedSwaps)
        {
            int a = swap[0];
            int b = swap[1];
            graph[a].Add(b);
            graph[b].Add(a);
        }

        HashSet<int> visited = new HashSet<int>();
        int result = 0;
        for (int i = 0; i < source.Length; i++)
        {
            if (!visited.Contains(i))
            {
                Queue<int> dq = new Queue<int>();
                HashSet<int> local = new HashSet<int>();
                dq.Enqueue(i);
                local.Add(i);

                while (dq.Count > 0)
                {
                    int node = dq.Dequeue();
                    foreach (int nxt in graph[node])
                    {
                        if (!local.Contains(nxt))
                        {
                            dq.Enqueue(nxt);
                            local.Add(nxt);
                        }
                    }
                }

                Dictionary<int, int> sourceDict = new Dictionary<int, int>();
                Dictionary<int, int> targetDict = new Dictionary<int, int>();
                foreach (int j in local)
                {
                    int targetValue = target[j];
                    int sourceValue = source[j];
                    
                    if (!targetDict.ContainsKey(targetValue))
                        targetDict[targetValue] = 0;
                    if (!sourceDict.ContainsKey(sourceValue))
                        sourceDict[sourceValue] = 0;

                    sourceDict[sourceValue]++;
                    targetDict[targetValue]++;
                }

                foreach (var kvp in targetDict)
                {
                    int key = kvp.Key;
                    int targetCount = kvp.Value;
                    int sourceCount = sourceDict.ContainsKey(key) ? sourceDict[key] : 0;
                    result += Math.Max(0, targetCount - sourceCount);
                }

                visited.UnionWith(local);
            }
        }

        return result;    
    }
}
// @lc code=end

