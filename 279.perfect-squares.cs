/*
 * @lc app=leetcode id=279 lang=csharp
 *
 * [279] Perfect Squares
 */

// @lc code=start
public class Solution 
{
    public int NumSquares(int n) 
    {
        HashSet<int> perfect = new HashSet<int>();
        for (int i = 1; i < 101; i++)
        {
            perfect.Add(i*i);
            if (i*i == n)
            {
                return 1;
            }
        }
        foreach (int item in perfect)
        {
            if (perfect.Contains(n - item))
            {
                return 2;
            }
        }
        while (n % 4 == 0)
        {
            n /= 4;
        }
        if (n % 8 == 7)
        {
            return 4;
        }
        else
        {
            return 3;
        }
    }
}
// @lc code=end

