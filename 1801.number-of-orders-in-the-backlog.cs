/*
 * @lc app=leetcode id=1801 lang=csharp
 *
 * [1801] Number of Orders in the Backlog
 */

// @lc code=start
public class Solution {
    public int GetNumberOfBacklogOrders(int[][] orders) {
        PriorityQueue<int, int>[] transactions = new PriorityQueue<int, int>[2];
        transactions = transactions.Select(x => new PriorityQueue<int, int> ()).ToArray();
        long MOD = 1000000007;
        foreach (int[] order in orders) 
        {
            int a = order[1];
            while (a > 0 && transactions[1 - order[2]].TryPeek(out int a1, out int p1) && p1 <= (order[2] == 0 ? 1 : -1) * order[0])
            {
                transactions[1 - order[2]].Dequeue();
                int deduct = Math.Min(a1, a);
                a1 -= deduct;
                a -= deduct;
                if (a1 > 0)
                {
                    transactions[1 - order[2]].Enqueue(a1, p1);
                }
            }
            if (a > 0)
            {
                transactions[order[2]].Enqueue(a, order[0] * (order[2] == 0 ? -1 : 1));
            }
        }

        long result = 0;
        for (int i = 0; i < 2; i++)
        {
            while (transactions[i].TryDequeue(out int a, out int p))
            {
                result += (long)a;
                result %= MOD;
            }
        }
        return Convert.ToInt32(result);
    }
}
// @lc code=end

