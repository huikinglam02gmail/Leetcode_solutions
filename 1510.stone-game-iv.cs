/*
 * @lc app=leetcode id=1510 lang=csharp
 *
 * [1510] Stone Game IV
 */

// @lc code=start
public class Solution 
{
    public bool WinnerSquareGame(int n) 
    {
        bool[] dp = new bool[n+1];
        Array.Fill(dp, false);
        List<int> perfectSquares = new List<int>();
        int x = 1;
        for (int i = 1; i < n + 1; i++)
        {
            if (x*x == i)
            {
                dp[i] = true;
                perfectSquares.Add(i);
                x++;
            }
            else
            {
                int j = 0;
                while (j < perfectSquares.Count)
                {
                    if (!dp[i - perfectSquares[j]])
                    {
                        dp[i] = true;
                        break;
                    }
                    else
                    {
                        j++;
                    }
                }
            }
        }
        return dp[n];
    }
}
// @lc code=end

