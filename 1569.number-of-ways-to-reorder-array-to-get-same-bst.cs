/*
 * @lc app=leetcode id=1569 lang=csharp
 *
 * [1569] Number of Ways to Reorder Array to Get Same BST
 */

// @lc code=start
using System.Collections.Generic;
public class Solution 
{
    private List<List<long>> nCr;
    private const long MOD = 1000000007;

    private void initiatenCr(int n)
    {
        nCr = new List<List<long>>();
        List<long> row = new List<long>() { 1 };
        nCr.Add(row);
        row = new List<long>() { 1, 2, 1 };
        nCr.Add(row);
        for (int i = 2; i < n; i++)
        {
            row = new List<long>() { 1 };
            for (int j = 0; j < nCr.Last().Count - 1; j++)
            {
                row.Add((nCr.Last()[j] + nCr.Last()[j + 1]) % MOD);
            }
            row.Add(1);
            nCr.Add(row);
        }
    }

    public long divideAndConquer(int[] arr)
    {
        int n = arr.Length; 
        if (arr.Length < 3)
        {
            return 1;
        }
        int root = arr[0];
        List<int> left = new List<int>();
        List<int> right = new List<int>();
        for (int i = 1; i < n; i++)
        {
            if (arr[i] < root)
            {
                left.Add(arr[i]);
            }
            else
            {
                right.Add(arr[i]);
            }
        }
        int nl = left.Count;
        return (((nCr[n - 2][nl] % MOD) * divideAndConquer(left.ToArray())) % MOD * (divideAndConquer(right.ToArray()))) % MOD; 
    }
    
    public int NumOfWays(int[] nums) 
    {
        initiatenCr(nums.Length);
        return Convert.ToInt32(divideAndConquer(nums) - 1);
    }
}
// @lc code=end
