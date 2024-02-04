/*
 * @lc app=leetcode id=76 lang=csharp
 *
 * [76] Minimum Window Substring
 */

// @lc code=start
using System;
using System.Collections.Generic;

public class Solution {
    public string MinWindow(string s, string t) {
        Dictionary<char, int> need = new Dictionary<char, int>();
        int missing = t.Length, i = 0, I = -1, J = -1;

        foreach (char c in t) {
            if (need.ContainsKey(c)) {
                need[c]++;
            } else {
                need[c] = 1;
            }
        }

        for (int j = 0; j < s.Length; j++) {
            char c = s[j];
            if (!need.ContainsKey(c)) need[c] = 0;
            if (need[c] > 0) {
                missing--;
            }
            need[c]--;

            if (missing == 0) {
                while (i < j && (need.ContainsKey(s[i]) && need[s[i]] < 0)) {
                    need[s[i]]++;
                    i++;
                }

                if (J == -1 || j - i <= J - I) {
                    I = i;
                    J = j;
                }
            }
        }

        if (missing == 0) {
            return s.Substring(I, J - I + 1);
        } else {
            return "";
        }
    }
}

// @lc code=end

