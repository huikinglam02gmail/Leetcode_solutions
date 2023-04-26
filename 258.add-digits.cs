/*
 * @lc app=leetcode id=258 lang=csharp
 *
 * [258] Add Digits
 */

// @lc code=start
public class Solution 
{
    public int AddDigits(int num) 
    {
        if (num < 10)
        {
            return num;
        }   
        else
        {
            int result = 0;
            foreach (char c in num.ToString())
            {
                result += (int)c - (int)'0';
            }
            return AddDigits(result);
        }
    }
}
// @lc code=end

