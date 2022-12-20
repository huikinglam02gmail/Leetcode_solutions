/*
 * @lc app=leetcode id=1551 lang=csharp
 *
 * [1551] Minimum Operations to Make Array Equal
 */

// @lc code=start
public class Solution 
{
    public int MinOperations(int n) 
    {
        if (n % 2 == 0)
        {
            return n * (n / 2) / 2;
        }
        else
        {
            return (n + 1)*(n / 2) / 2;
        }
    }
}
// @lc code=end

