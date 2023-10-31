/*
 * @lc app=leetcode id=2433 lang=csharp
 *
 * [2433] Find The Original Array of Prefix Xor
 */

// @lc code=start
using System;
using System.Collections.Generic;

public class Solution {
    public int[] FindArray(int[] pref) {
        int n = pref.Length;
        for (int i = n - 1; i > 0; i--) {
            pref[i] ^= pref[i - 1];
        }
        return pref;
    }
}

// @lc code=end

