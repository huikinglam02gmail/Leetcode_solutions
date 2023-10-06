/*
 * @lc app=leetcode id=1928 lang=csharp
 *
 * [1928] Minimum Cost to Reach Destination in Time
 */

// @lc code=start
public class Solution {
public int MinCost(int maxTime, int[][] edges, int[] passingFees) {
        int n = passingFees.Length;
        List<int[]>[] graph = new List<int[]>[n];
        for (int i = 0; i < n; i++) {
            graph[i] = new List<int[]>();
        }
        
        foreach (var edge in edges) {
            int x = edge[0];
            int y = edge[1];
            int time = edge[2];
            graph[x].Add(new int[2] { y, time});
            graph[y].Add(new int[2] { x, time});
        }
        
        PriorityQueue<int[], int> pq = new PriorityQueue<int[], int>();
        int[] arrivals = new int[n];
        Array.Fill(arrivals, int.MaxValue);
        pq.Enqueue(new int[2]{0, 0}, passingFees[0]);
        
        while (pq.TryDequeue(out int[] info, out int cost)) {
            int node = info[0];
            int time = info[1];
            
            if (time > maxTime) {
                continue;
            }
            
            if (node == n - 1) {
                return cost;
            }
            
            if (time < arrivals[node]) {
                arrivals[node] = time;
                foreach (int[] neighbor in graph[node]) {
                    pq.Enqueue(new int[2]{neighbor[0], time + neighbor[1]}, passingFees[neighbor[0]] + cost);
                }
            }
        }
        
        return -1;
    }
}
// @lc code=end

