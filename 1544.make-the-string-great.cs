/*
 * @lc app=leetcode id=1544 lang=csharp
 *
 * [1544] Make The String Great
 */

// @lc code=start
public class Solution {
    public string MakeGood(string s) {
        Stack<char> result = new Stack<char>();
        foreach (char c in s)
        {
            if (result.Count > 0 && Math.Abs((int) c - (int) result.Peek()) == 32)
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
        return string.Join("", resultArray);
    }
}
// @lc code=end

