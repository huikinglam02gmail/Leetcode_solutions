/*
 * @lc app=leetcode id=1345 lang=csharp
 *
 * [1345] Jump Game IV
 */

// @lc code=start
using System.Collections.Generic;
public class Solution 
{
    public int MinJumps(int[] arr) 
    {
        int n = arr.Length;
        Dictionary<int, List<int>> hashTable = new Dictionary<int, List<int>>();
        for (int i = 0; i < n; i++)
        {
            if (!hashTable.ContainsKey(arr[i]))
            {
                hashTable.Add(arr[i], new List<int>());
            }
            hashTable[arr[i]].Add(i);
        }
        
        Queue<int> queue = new Queue<int>();
        bool[] visited = new bool[n];
        Array.Fill(visited, false);
        HashSet<int> visitedValues = new HashSet<int>();
        int steps = 0;
        queue.Enqueue(0);
        visited[0] = true;
        while (queue.Count > 0)
        {
            int m = queue.Count;
            for (int i = 0; i < m; i++)
            {
                int node = queue.Dequeue();
                if (node == n - 1)
                {
                    return steps;
                }
                if (!visitedValues.Contains(arr[node]))
                {
                    foreach (int nxt in hashTable[arr[node]])
                    {
                        if (!visited[nxt])
                        {
                            queue.Enqueue(nxt);
                            visited[nxt] = true;
                        }
                    }
                    visitedValues.Add(arr[node]);
                }
                if (node > 0 && !visited[node - 1])
                {
                    queue.Enqueue(node - 1);
                    visited[node - 1] = true;
                }
                if (!visited[node + 1])
                {
                    queue.Enqueue(node + 1);
                    visited[node + 1] = true;
                }
            }
            steps++;
        }
        return -1;
    }
}
// @lc code=end

