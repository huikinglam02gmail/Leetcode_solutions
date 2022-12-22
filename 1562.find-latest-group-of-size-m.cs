/*
 * @lc app=leetcode id=1562 lang=csharp
 *
 * [1562] Find Latest Group of Size M
 */

// @lc code=start
// We can also mark the boundary of each point as it evolve
// Any new points added will always be bordered by previous boundaries
public class Solution 
{
    public int FindLatestStep(int[] arr, int m) 
    {
        int n = arr.Length;
        if (m == n)
        {
            return m;
        }
        
        int[] l = new int[n + 2];
        Array.Fill(l, 0);
        int result = -1;
        for (int i = 0; i < n; i++)
        {
            int left = l[arr[i] - 1];
            int right = l[arr[i] + 1];
            if (left == m || right == m)
            {
                result = i;
            }
            l[arr[i] - left] = left + right + 1;
            l[arr[i] + right] = left + right + 1;
        }
        return result;
    }
}
// @lc code=end

