/*
 * @lc app=leetcode id=2509 lang=csharp
 *
 * [2509] Cycle Length Queries in a Tree
 */

// @lc code=start
public class Solution 
{
    public int[] CycleLengthQueries(int n, int[][] queries) 
    {
        int m = queries.Length;
        int[] result = new int[m];
        for (int i = 0; i < m; i++)
        {
            Dictionary<int, int> aDict = new Dictionary<int, int>();
            int aCount = 0;
            int bCount = 0;
            int a = queries[i][0];
            int b = queries[i][1];
            while (a != 0)
            {
                aDict[a] = aCount;
                aCount++;
                a /= 2;
            }
            while (!aDict.ContainsKey(b))
            {
                bCount++;
                b /= 2;
            }
            result[i] = 1 + aDict[b] + bCount;
        }
        return result;
    }
}
// @lc code=end

