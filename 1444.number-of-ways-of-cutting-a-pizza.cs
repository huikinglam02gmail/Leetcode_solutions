/*
 * @lc app=leetcode id=1444 lang=csharp
 *
 * [1444] Number of Ways of Cutting a Pizza
 */

// @lc code=start
public class Solution 
{
    int[][] P;
    int m;
    int n;
    long MOD = 100000007;
    Dictionary<Tuple<int,int,int>, long> memo = new Dictionary<Tuple<int,int,int>, long>();
    int sumRegion(int row1, int col1, int row2, int col2)
    {
        return P[row2+1][col2+1] + P[row1][col1] - P[row1][col2+1] - P[row2+1][col1];
    }

    long dp(int i, int j, int c)
    {
        Tuple<int, int, int> key = new Tuple<int, int, int>(i, j, c);
        if (memo.ContainsKey(key))
        {
            return memo[key];
        }
        else
        {
            long result;
            if (c == 0)
            {
                if (sumRegion(i, j, m-1, n-1) >= 1)
                {
                    return 1;
                }
                else
                {
                    return 0;
                }
            }
            if (sumRegion(i, j, m-1, n-1) == 0)
            {
                return 0;
            }
            else
            {
                result = 0;
                for (int l = 1; l < m + 1; l++)
                {
                    if (sumRegion(i, j, l-1, n-1) >= 1)
                    {
                        result += dp(l, j, c - 1);
                    }
                }
                for (int l = 1; l < n + 1; l++)
                {
                    if (sumRegion(i, j, m-1, l-1) >= 1)
                    {
                        result += dp(i, l, c - 1);
                    }
                }
            }
            memo.Add(key, result);
            Console.WriteLine($"{key}, {result}");
            return result;
        }
    }
    public int Ways(string[] pizza, int k) 
    {
        m = pizza.Length;
        n = pizza[0].Length;
        P = new int[m+1][];
        for (int i = 0; i < m + 1; i++)
        {
            P[i] = new int[n+1];
            Array.Fill(P[i], 0);
        }
        for (int i = 1; i< m + 1; i++)
        {
            for (int j = 1; j < n + 1; j++)
            {
                P[i][j] = P[i-1][j] + P[i][j-1] - P[i-1][j-1];
                if (pizza[i-1][j-1] == 'A')
                {
                    P[i][j] += 1;
                }
            }
        }
        return Convert.ToInt32(dp(0,0,k-1) % MOD);
    }
}
// @lc code=end

