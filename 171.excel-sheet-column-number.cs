/*
 * @lc app=leetcode id=171 lang=csharp
 *
 * [171] Excel Sheet Column Number
 */

// @lc code=start
public class Solution {
    public int TitleToNumber(string columnTitle) {
        int n = columnTitle.Length;
        int value = 0;
        int factor = 1;
        
        for (int i = n - 1; i >= 0; i--) {
            char c = columnTitle[i];
            value += (c - 'A' + 1) * factor;
            factor *= 26;
        }
        
        return value;
    }
}
// @lc code=end

