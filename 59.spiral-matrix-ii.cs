/*
 * @lc app=leetcode id=59 lang=csharp
 *
 * [59] Spiral Matrix II
 */

// @lc code=start
using System.Linq;
public class Solution 
{
    public int[][] GenerateMatrix(int n) 
    {
        int state = 0;
        int count = 0;
        int[][] result = new int[n][];
        result = result.Select(x => new int[n]).ToArray();
        int i = 0;
        int j = 0;
        int[][] nxt = new int[4][];
        while (count < n*n)
        {
            count++;
            result[i][j] = count;
            if (count == n*n)
            {
                break;
            }
            nxt[0] = new int[2] { i, j + 1};
            nxt[1] = new int[2] { i + 1, j};
            nxt[2] = new int[2] { i, j - 1};
            nxt[3] = new int[2] { i - 1, j};
            if (nxt[state][0] < 0 || nxt[state][0] >= n || nxt[state][1] >= n || nxt[state][1] < 0 || result[nxt[state][0]][nxt[state][1]] > 0)
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

