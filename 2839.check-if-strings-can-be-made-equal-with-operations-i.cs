/*
 * @lc app=leetcode id=2839 lang=csharp
 *
 * [2839] Check if Strings Can be Made Equal With Operations I
 */

// @lc code=start
public class Solution {
    public bool CanBeEqual(string s1, string s2) {
        if (s1 == s2) return true;
        char[] strings = new char[] { s1[2], s1[1], s1[0], s1[3]};
        if (String.Concat(strings) == s2) return true;
        strings = new char[] { s1[2], s1[3], s1[0], s1[1]};
        if (String.Concat(strings) == s2) return true;      
        strings = new char[] { s1[0], s1[3], s1[2], s1[1]};
        if (String.Concat(strings) == s2) return true;
        return false;
    }
}

// @lc code=end

