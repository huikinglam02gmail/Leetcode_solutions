/*
 * @lc app=leetcode id=263 lang=csharp
 *
 * [263] Ugly Number
 */

// @lc code=start
public class Solution 
{
    public bool IsUgly(int n) 
    {
        if (n <= 0)
        {
            return false;
        }
        else if (n == 1)
        {
            return true;
        }
        else if (n % 2 == 0)
        {
            return IsUgly(n / 2);
        }
        else if (n % 3 == 0)
        {
            return IsUgly(n / 3);
        }
        else if (n % 5 == 0)
        {
            return IsUgly(n / 5);
        }
        return false;
    }
}
// @lc code=end

