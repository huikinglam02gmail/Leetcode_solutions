/*
 * @lc app=leetcode id=2437 lang=csharp
 *
 * [2437] Number of Valid Clock Times
 */

// @lc code=start
using System;
using System.Collections.Generic;

public class Solution {
    /*
    Just try whatever combinations
    */
    public bool ValidTime(string time) {
        if (int.Parse(time.Substring(0, 2)) > 23 || int.Parse(time.Substring(3)) > 59) {
            return false;
        }
        return 0 <= int.Parse(time.Substring(0, 2)) * 60 + int.Parse(time.Substring(3)) && int.Parse(time.Substring(0, 2)) * 60 + int.Parse(time.Substring(3)) <= 23 * 60 + 59;
    }
    
    public int CountTime(string time) {
        List<string> pos = new List<string>();
        pos.Add("");
        foreach (char c in time) {
            List<string> newPos = new List<string>();
            if (c != '?') {
                foreach (string p in pos) {
                    newPos.Add(p + c);
                }
            } else {
                foreach (string p in pos) {
                    for (int i = 0; i < 10; i++) {
                        newPos.Add(p + i);
                    }
                }
            }
            pos = newPos;
        }
        int result = 0;
        foreach (string p in pos) {
            if (ValidTime(p)) {
                result++;
            }
        }
        return result;
    }
}

// @lc code=end

