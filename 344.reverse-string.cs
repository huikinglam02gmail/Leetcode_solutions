/*
 * @lc app=leetcode id=344 lang=csharp
 *
 * [344] Reverse String
 */

// @lc code=start
public class Solution {
    public void ReverseString(char[] s) {
        int l = 0;
        int r = s.Length - 1;
        while (l < r)
        {
            char c = s[l];
            s[l] = s[r];
            s[r] = c;
            l++;
            r--; 
        }
    }
}
// @lc code=end

