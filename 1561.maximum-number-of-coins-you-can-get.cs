/*
 * @lc app=leetcode id=1561 lang=csharp
 *
 * [1561] Maximum Number of Coins You Can Get
 */

// @lc code=start
public class Solution 
{
    public int MaxCoins(int[] piles)
    {
        int n = piles.Length;
        int result = 0;
        Array.Sort(piles);
        for (int i = n - 2; i > n / 3 - 1; i-=2)
        {
            result += piles[i];
        }
        return result;
    }
}
// @lc code=end

