/*
 * @lc app=leetcode id=1504 lang=csharp
 *
 * [1504] Count Submatrices With All Ones
 */

// @lc code=start
public class Solution 
{
    public int NumSubmat(int[][] mat) 
    {
        int m = mat.Length;
        int n = mat[0].Length;
        int[] last = new int[n];
        int[] BR = new int[n];
        Stack<int> stack = new Stack<int>();
        int result = 0;

        Array.Fill(last, 0);
        for (int i = 0; i < m; i++)
        {
            stack.Clear();
            Array.Fill(BR, 0);
            for (int j = 0; j < n; j++)
            {
                if (mat[i][j] == 1)
                {
                    last[j]++;
                }
                else
                {
                    last[j] = 0;
                }
                while (stack.TryPeek(out int l) && last[j] <= last[l])
                {
                    stack.Pop();
                }
                if (stack.TryPeek(out int l1))
                {
                    BR[j] += last[j]*(j - l1);
                    BR[j] += BR[l1];
                }
                else
                {
                    BR[j] += last[j]* (j+1);
                }
                stack.Push(j);
                result += BR[j];
            }
        }
        return result;
    }
}
// @lc code=end

