/*
 * @lc app=leetcode id=455 lang=csharp
 *
 * [455] Assign Cookies
 */

// @lc code=start
using System;
using System.Collections.Generic;

public class Solution {
    public int FindContentChildren(int[] g, int[] s) {
        Array.Sort(g);
        Array.Sort(s);

        int content = 0;
        int ps = 0;

        while (content < g.Length && ps < s.Length) {
            if (s[ps] >= g[content]) {
                content++;
            }
            ps++;
        }

        return content;
    }
}

// @lc code=end

