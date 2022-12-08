/*
 * @lc app=leetcode id=1514 lang=csharp
 *
 * [1514] Path with Maximum Probability
 */

// @lc code=start
/*
 * @lc app=leetcode id=1514 lang=csharp
 *
 * [1514] Path with Maximum Probability
 */

// @lc code=start
public class Solution 
{
    public double MaxProbability(int n, int[][] edges, double[] succProb, int start, int end) 
    {
        HashSet<Tuple<int, double>>[] graph = new HashSet<Tuple<int, double>>[n];
        PriorityQueue<int, double> heap = new PriorityQueue<int, double>();
        double[] cost = new double[n];
        Array.Fill(cost, Double.PositiveInfinity);
        for (int i = 0; i < n; i++)
        {
            graph[i] = new HashSet<Tuple<int, double>>();
        }
        for (int i = 0; i < edges.Length; i++)
        {
            int a = edges[i][0];
            int b = edges[i][1];
            double w = Double.PositiveInfinity;
            if (succProb[i] > 0)
            {
                w = - Math.Log(succProb[i]);
            }
            graph[a].Add(new Tuple<int, double>(b, w));
            graph[b].Add(new Tuple<int, double>(a, w));
        }

        heap.Enqueue(start, 0);
        cost[start] = 0;
        while (heap.TryDequeue(out int node, out double P))
        {
            if (node == end)
            {
                return Math.Exp(- P);
            }
            foreach (Tuple<int, double> t in graph[node])
            {
                if (P + t.Item2 < cost[t.Item1])
                {
                    heap.Enqueue(t.Item1, P + t.Item2);
                    cost[t.Item1] = P + t.Item2;
                }
            }
        }
        return 0;
    }
}
// @lc code=end
// @lc code=end