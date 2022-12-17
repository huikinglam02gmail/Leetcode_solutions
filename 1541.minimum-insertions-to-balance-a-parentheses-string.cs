/*
 * @lc app=leetcode id=1541 lang=csharp
 *
 * [1541] Minimum Insertions to Balance a Parentheses String
 */

// @lc code=start
public class Solution 
{
    public int MinInsertions(string s) 
    {
        int open = 0;
        int result = 0;
        s = s.Replace("))", "}");
        foreach (char c in s)
        {
            if (c == '(')
            {
                open++;
            }
            else if (c == '}')
            {
                if (open > 0)
                {
                    open--;
                }
                else
                {
                    result++;
                }
            }
            else
            {
                if (open > 0)
                {
                    open--;
                }
                else
                {
                    result++;
                }
                result++;
            }
        }
        return result + open*2;    
    }
}
// @lc code=end

