/*
 * @lc app=leetcode id=1563 lang=csharp
 *
 * [1563] Stone Game V
 */

// @lc code=start
public class Solution 
{
    public int StoneGameV(int[] stoneValue) 
    {
        int n = stoneValue.Length;
        int[,] dp = new int[n,n];
        int[,] score = new int[n,n];
        for (int j = 0; j < n; j ++)
        {
            int mid = j;
            int S = 0;
            int rightHalf = 0;
            for (int i = j; i >= 0; i--)
            {
                S += stoneValue[i];
                if (i == j)
                {
                    score[i, j] = stoneValue[i];
                }
                else
                {
                    while ((rightHalf + stoneValue[mid])*2 <= S)
                    {
                        rightHalf += stoneValue[mid];
                        mid--;
                    }
                    if (2*rightHalf == S)
                    {
                        dp[i,j] = score[i, mid];
                    }
                    else if (mid != i)
                    {
                        dp[i,j] = score[i, mid-1];
                    }
                    if (mid != j)
                    {
                        dp[i,j] = Math.Max(dp[i,j], score[j, mid+1]);
                    }
                    score[i,j] = Math.Max(score[i, j-1], dp[i, j] + S);
                    score[j,i] = Math.Max(score[j, i+1], dp[i, j] + S);
                }
            }
        }
        return dp[0, n-1];
    }
}
// @lc code=end

