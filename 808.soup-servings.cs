/*
 * @lc app=leetcode id=808 lang=csharp
 *
 * [808] Soup Servings
 */

// @lc code=start
using System;

public class Solution
{
    /*
     * Operation 1: A -= 100
     * Operation 2: A -= 75, B -= 25
     * Operation 3: A -= 50, B -= 50
     * Operation 4: A -= 25, B -= 75
     * Maintain status of A and B and round.
     * Since after each round, the modification will add 1/(4^k) to the probability.
     * We can see that when n becomes large, the answer goes towards 1.
     * To find out the exact limit I manually binary search on the n threshold and found it to be 4801.
     */
    private Dictionary<Tuple<int, int, int>, double> memo;
    private double Dfs(int A, int B, int k)
    {
        if (A <= 0 && B > 0)
            return 1 / Math.Pow(4, k);
        if (A <= 0 && B <= 0)
            return 1 / (2 * Math.Pow(4, k));
        if (A > 0 && B <= 0)
            return 0;
        Tuple<int, int, int> t = new Tuple<int, int, int> (A, B, k);
        if (!memo.ContainsKey (t))
        {
            double result = 0;
            result += Dfs(A - 100, B, k + 1);
            result += Dfs(A - 75, B - 25, k + 1);
            result += Dfs(A - 50, B - 50, k + 1);
            result += Dfs(A - 25, B - 75, k + 1);
            memo.Add(t, result);
        }
        return memo[t];
    }

    public double SoupServings(int n)
    {
        memo = new Dictionary<Tuple<int, int, int>, double>();
        return n > 4800 ? 1 : Dfs(n, n, 0);
    }
}

// @lc code=end

