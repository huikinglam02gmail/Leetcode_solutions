/*
 * @lc app=leetcode id=392 lang=csharp
 *
 * [392] Is Subsequence
 */

// @lc code=start
public class Solution {
    public bool IsSubsequence(string s, string t) {
        int p1 = 0, p2 = 0;
        while (p1 < s.Length && p2 < t.Length) {
            if (s[p1] == t[p2]) {
                p1++;
            }
            p2++;
        }
        return p1 == s.Length;
    }
}

// @lc code=end

