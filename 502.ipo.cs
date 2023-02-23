/*
 * @lc app=leetcode id=502 lang=csharp
 *
 * [502] IPO
 */

// @lc code=start
public class Solution 
{
    public int FindMaximizedCapital(int k, int w, int[] profits, int[] capital) 
    {
        List<int[]> couples = new List<int[]>();
        PriorityQueue<int, int> queue = new PriorityQueue<int, int>();
        int n = profits.Length;
        for (int j = 0; j < n; j++)
        {
            couples.Add(new int[2] {capital[j], profits[j]});
        }
        couples = couples.OrderBy(x => x[0]).ToList();
        int i = 0;
        while (k > 0)
        {
            while (i < couples.Count && couples[i][0] <= w)
            {
                queue.Enqueue(couples[i][1], - couples[i][1]);
                i++;
            }
            if (queue.Count == 0)
            {
                return w;
            }
            w += queue.Dequeue();
            k--;
        }
        return w;
    }
}
// @lc code=end

