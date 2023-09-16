/*
 * @lc app=leetcode id=1898 lang=csharp
 *
 * [1898] Maximum Number of Removable Characters
 */

// @lc code=start
using System;
using System.Collections.Generic;

public class Solution {
    private Dictionary<int, int> reverseRemovable;
    public bool IsSubsequence(string s, string t, int mid) {
        int p1 = 0, p2 = 0;
        while (p1 < s.Length && p2 < t.Length) {
            if (s[p1] == t[p2] && (!reverseRemovable.ContainsKey(p2) || reverseRemovable[p2] >= mid)) {
                p1++;
            }
            p2++;
        }
        return p1 == s.Length;
    }

    public int MaximumRemovals(string s, string p, int[] removable) {
        int l = 0, r = removable.Length;
        reverseRemovable = new Dictionary<int, int>();
        for (int i = 0; i < removable.Length; i++) {
            reverseRemovable[removable[i]] = i;
        }
        while (l < r) {
            int mid = l + (r - l) / 2;
            if (IsSubsequence(p, s, mid)) {
                l = mid + 1;
            } else {
                r = mid;
            }
        }
        if (l == removable.Length && IsSubsequence(p, s, l)) {
            return l;
        } else {
            return l - 1;
        }
    }
}


// @lc code=end

