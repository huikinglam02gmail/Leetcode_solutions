/*
 * @lc app=leetcode id=54 lang=csharp
 *
 * [54] Spiral Matrix
 */

// @lc code=start
using System.Collections.Generic;
public class Solution 
{
    public IList<int> SpiralOrder(int[][] matrix) 
    {
        int state = 0;
        int count = 0;
        List<int> result = new List<int>();
        int i = 0;
        int j = 0;
        int m = matrix.Length;
        int n = matrix[0].Length;
        int[][] nxt = new int[4][];
        while (result.Count < m * n)
        {
            result.Add(matrix[i][j]);
            matrix[i][j] -= 201;
            if (count == m * n)
            {
                break;
            }
            nxt[0] = new int[2] { i, j + 1};
            nxt[1] = new int[2] { i + 1, j};
            nxt[2] = new int[2] { i, j - 1};
            nxt[3] = new int[2] { i - 1, j};
            if (nxt[state][0] < 0 || nxt[state][0] >= m || nxt[state][1] >= n || nxt[state][1] < 0 || matrix[nxt[state][0]][nxt[state][1]] < - 100)
            {
                state++;
                state %= 4;
            }
            i = nxt[state][0];
            j = nxt[state][1];
        }
        return result;        
    }
}
// @lc code=end

