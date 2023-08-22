/*
 * @lc app=leetcode id=168 lang=csharp
 *
 * [168] Excel Sheet Column Title
 */

// @lc code=start
public class Solution {
    public string ConvertToTitle(int columnNumber) {
        string result = "";
        while (columnNumber > 0) {
            result += (char)((columnNumber - 1) % 26 + 'A');
            columnNumber = (columnNumber - 1) / 26;
        }
        char[] charArray = result.ToCharArray();
        Array.Reverse(charArray);
        return new string(charArray);
    }
}

// @lc code=end

