/*
 * @lc app=leetcode id=1903 lang=csharp
 *
 * [1903] Largest Odd Number in String
 */

// @lc code=start
public class Solution
{
    public string LargestOddNumber(string num)
    {
        for (int i = num.Length - 1; i >= 0; i--)
        {
            if (int.Parse(num[i].ToString()) % 2 == 1)
            {
                return num.Substring(0, i + 1);
            }
        }
        return string.Empty;
    }
}

// @lc code=end

