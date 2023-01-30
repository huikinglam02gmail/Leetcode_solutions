/*
 * @lc app=leetcode id=1137 lang=csharp
 *
 * [1137] N-th Tribonacci Number
 */

// @lc code=start
public class Solution 
{
    public int Tribonacci(int n) 
    {
        int[] t = new int[4]{0, 1, 1, 2};
        if (n < 4)
        {
            return t[n];
        }
        else
        {
            int[] tNew = new int[4];
            for (int i = 3; i < n; i++)
            {
                Array.Copy(t, 1, tNew, 0, 3);
                tNew[3] = tNew[0] + tNew[1] + tNew[2];
                Array.Copy(tNew, 0, t, 0, 4);
            }
            return t[3];
        }
    }
}
// @lc code=end

