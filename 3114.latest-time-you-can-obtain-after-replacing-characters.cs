/*
 * @lc app=leetcode id=3114 lang=csharp
 *
 * [3114] Latest Time You Can Obtain After Replacing Characters
 */

// @lc code=start
using System;
using System.Collections.Generic;

public class Solution {
    /*
    Generate all possible times
    Try to match
    */
    private List<string> result;

    public Solution() {
        result = new List<string>();
        for (int i = 719; i >= 0; i--) {
            result.Add((i / 60).ToString("D2") + ":" + (i % 60).ToString("D2"));
        }
    }

    public string FindLatestTime(string s) {
        foreach (string t in result) {
            if ((s[0] == '?' || s[0] == t[0]) && 
                (s[1] == '?' || s[1] == t[1]) && 
                (s[3] == '?' || s[3] == t[3]) && 
                (s[4] == '?' || s[4] == t[4])) {
                return t;
            }
        }
        return "";
    }
}

// @lc code=end

