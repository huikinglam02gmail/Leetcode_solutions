/*
 * @lc app=leetcode id=1595 lang=csharp
 *
 * [1595] Minimum Cost to Connect Two Groups of Points
 */

// @lc code=start
public class Solution 
{
    List<IList<int>> Cost;
    int[] minCost;
    Dictionary<Tuple<int, int>, int> memo;

    public int dp(int i, int mask)
    {
        Tuple<int, int> t = new Tuple<int, int>(i, mask);
        int result;
        if (memo.ContainsKey(t))
        {
            return memo[t];
        }
        else if (i == Cost.Count)
        {
            result = 0;
            for (int j = 0; j < Cost[0].Count; j++)
            {
                if ((mask & (1 << j)) == 0)
                {
                    result += minCost[j];
                }
            }
        }
        else
        {
            result = Int32.MaxValue;
            for (int j = 0; j < Cost[0].Count; j++)
            {
                result = Math.Min(result, Cost[i][j] + dp(i + 1, mask | (1 << j)));
            }
        }
        memo.Add(t, result);
        return result;
    }

    public int ConnectTwoGroups(IList<IList<int>> cost) 
    {
        Cost = cost.ToList();
        int m = Cost.Count;
        int n = Cost[0].Count;
        minCost = new int[n];
        Array.Fill(minCost, 100);
        for (int j = 0; j < n; j++)
        {
            for (int i = 0; i < m; i++)
            {
                minCost[j] = Math.Min(minCost[j], Cost[i][j]);
            }
        }
        memo = new Dictionary<Tuple<int, int>, int>();
        return dp(0, 0);
    }
}
// @lc code=end
