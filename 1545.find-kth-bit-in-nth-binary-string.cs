/*
 * @lc app=leetcode id=1545 lang=csharp
 *
 * [1545] Find Kth Bit in Nth Binary String
 */

// @lc code=start
public class Solution 
{
    public char FindKthBit(int n, int k) 
    {
        if (n == 1)
        {
            return '0';
        }
        if (k == (int) Math.Pow(2, n - 1))
        {
            return '1';
        }
        else if (k > (int) Math.Pow(2, n - 1))
        {
            return Convert.ToChar(1 - (int) FindKthBit(n - 1, (int) Math.Pow(2, n) - k) + 2*(int) '0');
        }
        else
        {
            return FindKthBit(n - 1, k);
        }
    }
}
// @lc code=end

