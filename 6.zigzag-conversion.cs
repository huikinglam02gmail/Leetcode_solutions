/*
 * @lc app=leetcode id=6 lang=csharp
 *
 * [6] Zigzag Conversion
 */

// @lc code=start
public class Solution
{
    public string Convert(string s, int numRows) 
    {
        if (numRows == 1)
        {
            return s;
        }    

        List<char>[] rows = new List<char>[numRows];
        for (int i = 0; i < numRows; i++)
        {
            rows[i] = new List<char>();
        }

        for (int i = 0; i < s.Length; i++)
        {
            if ((i % (2*(numRows - 1))) < numRows - 1)
            {
                rows[i % (2*(numRows - 1))].Add(s[i]);
            }
            else
            {
                rows[2*(numRows - 1) - (i % (2*(numRows - 1)))].Add(s[i]);
            }
        }

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < numRows; i++)
        {
            sb.Append(string.Join("", rows[i].ToArray()));
        }
        return sb.ToString();
    }
}
// @lc code=end

