/*
 * @lc app=leetcode id=1849 lang=csharp
 *
 * [1849] Splitting a String Into Descending Consecutive Values
 */

// @lc code=start
using System;
using System.Collections.Generic;

public class Solution {
    private string s;

    public bool Backtracking(int start, int end, long inFront) {
        if (inFront > 0 && long.TryParse(s.Substring(start, end - start + 1), out long total) && total == inFront - 1) {
            return true;
        }

        int i = start + 1;
        while (i < end + 1 && long.TryParse(s.Substring(start, i - start), out long front))
        {
            if (front.ToString().Length > end + 2 - i)
            {
                break;
            }
            else if ((inFront < 0 || inFront - 1 == front) && Backtracking(i, end, front)) 
            {
                return true;
            }
            else
            {
                ++i;
            }
        }
        return false;
    }

    public bool SplitString(string s) {
        this.s = s;
        int n = s.Length;
        return Backtracking(0, n - 1, -1);
    }
}

// @lc code=end

