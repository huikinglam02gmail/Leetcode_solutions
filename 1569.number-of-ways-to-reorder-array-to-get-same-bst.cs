/*
 * @lc app=leetcode id=1569 lang=csharp
 *
 * [1569] Number of Ways to Reorder Array to Get Same BST
 */

// @lc code=start

public class Solution 
{
    long MOD = 1000000007;

    long mod(long x, long m) 
    {
        return (x%m + m)%m;
    }

    public long comb(int n, int r)
    {
        if (n == r || r == 0)
        {
            return 1;
        }
        else
        {
            return mod(comb(n - 1, r - 1) + comb(n - 1, r), MOD);
        }
    }

    public long divideAndConquer(int[] arr)
    {
        int n = arr.Length;
        if (arr.Length < 2)
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
        return mod(mod(mod(comb(n-1, nl), MOD)*mod(divideAndConquer(left.ToArray()), MOD), MOD)*mod(divideAndConquer(right.ToArray()), MOD), MOD);
    }
    
    public int NumOfWays(int[] nums) 
    {
        return Convert.ToInt32(divideAndConquer(nums) - 1);
    }
}
// @lc code=end

