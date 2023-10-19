/*
 * @lc app=leetcode id=844 lang=csharp
 *
 * [844] Backspace String Compare
 */

// @lc code=start
/**
 * @lc app=leetcode id=844 lang=csharp
 *
 * [844] Backspace String Compare
 */

using System.Collections.Generic;

public class Solution {
    public bool BackspaceCompare(string s, string t) {
        List<char> sFinal = new List<char>();
        List<char> tFinal = new List<char>();

        foreach (char c in s) {
            if (c == '#') {
                if (sFinal.Count > 0) {
                    sFinal.RemoveAt(sFinal.Count - 1);
                }
            } else {
                sFinal.Add(c);
            }
        }

        foreach (char c in t) {
            if (c == '#') {
                if (tFinal.Count > 0) {
                    tFinal.RemoveAt(tFinal.Count - 1);
                }
            } else {
                tFinal.Add(c);
            }
        }

        if (sFinal.Count != tFinal.Count) {
            return false;
        }

        for (int i = 0; i < sFinal.Count; i++) {
            if (sFinal[i] != tFinal[i]) {
                return false;
            }
        }

        return true;
    }
}

// @lc code=end

