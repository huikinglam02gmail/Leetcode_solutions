/*
 * @lc app=leetcode id=3083 lang=csharp
 *
 * [3083] Existence of a Substring in a String and Its Reverse
 */

// @lc code=start
using System;

public class Solution {
    public bool IsSubstringPresent(string s) {
        char[] sReverse = s.ToCharArray();
        Array.Reverse(sReverse);
        string sReverseString = new string(sReverse);
        int n = s.Length;
        for (int i = 0; i < n - 1; i++) {
            string substr = s.Substring(i, 2);
            if (sReverseString.Contains(substr)) return true;
        }
        return false;
    }
}

// @lc code=end

