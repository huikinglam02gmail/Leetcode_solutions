/*
 * @lc app=leetcode id=1834 lang=csharp
 *
 * [1834] Single-Threaded CPU
 */

// @lc code=start
public class Solution 
{
    public int[] GetOrder(int[][] tasks) 
    {
        List<List<int>> data = new List<List<int>>();
        List<int> result = new List<int>();
        PriorityQueue<int, Tuple<int, int>> heap = new PriorityQueue<int, Tuple<int, int>>();
        for (int i = 0; i < tasks.Length; i++)
        {
            data.Add(new List<int>(){tasks[i][0], tasks[i][1], i});
        }
        data = data.OrderBy(x => x[0]).ToList();

        int globalTime = 0;
        int p = 0;
        int n = data.Count();
        while (p < n || heap.Count > 0)
        {
            if (heap.Count == 0)
            {
                globalTime = data[p][0];
                while (p < n && data[p][0] == globalTime)
                {
                    heap.Enqueue(data[p][2], new Tuple<int, int>(data[p][1],data[p][2]));
                    p++;
                }
            }
            if (heap.TryDequeue(out int ind, out Tuple<int, int> t))
            {
                globalTime += t.Item1;
                result.Add(ind);
                while (p < n && data[p][0] <= globalTime)
                {
                    heap.Enqueue(data[p][2], new Tuple<int, int>(data[p][1],data[p][2]));
                    p++;
                }
            }
        }
        return result.ToArray();
    }
}
// @lc code=end

