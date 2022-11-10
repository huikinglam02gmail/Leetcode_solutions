/*
 * @lc app=leetcode id=1047 lang=csharp
 *
 * [1047] Remove All Adjacent Duplicates In String
 */

// @lc code=start
public class Solution 
{
    public string RemoveDuplicates(string s) 
    {
        Stack<char> result = new Stack<char>();
        foreach(char c in s)
        {
            if (result.TryPeek(out char last) && last == c)
            {
                result.Pop();
            }
            else
            {
                result.Push(c);
            }
        }
        char[] resultArray = result.ToArray();
        Array.Reverse(resultArray);
        return new String(resultArray); 
    }
}
// @lc code=end

