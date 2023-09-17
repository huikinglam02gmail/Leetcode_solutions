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
    private string s;
    private string p;
    public bool IsSubsequence(int mid) {
        int p1 = 0, p2 = 0;
        while (p1 < p.Length && p2 < s.Length) {
            if (p[p1] == s[p2] && (!reverseRemovable.ContainsKey(p2) || reverseRemovable[p2] >= mid)) {
                p1++;
            }
            p2++;
        }
        return p1 == p.Length;
    }

    public int MaximumRemovals(string s, string p, int[] removable) {
        int l = 0, r = removable.Length;
        this.s = s;
        this.p = p;
        reverseRemovable = new Dictionary<int, int>();
        for (int i = 0; i < removable.Length; i++) {
            reverseRemovable[removable[i]] = i;
        }
        while (l < r) {
            int mid = l + (r - l) / 2;
            if (IsSubsequence(mid)) {
                l = mid + 1;
            } else {
                r = mid;
            }
        }
        if (l == removable.Length && IsSubsequence(l)) {
            return l;
        } else {
            return l - 1;
        }
    }
}


// @lc code=end

