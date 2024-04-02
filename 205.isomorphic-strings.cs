/*
 * @lc app=leetcode id=205 lang=csharp
 *
 * [205] Isomorphic Strings
 */

// @lc code=start
using System;
using System.Collections.Generic;

public class Solution {
    public bool IsIsomorphic(string s, string t) {
        Dictionary<char, char> hashTable = new Dictionary<char, char>();
        HashSet<char> seen = new HashSet<char>();
        for (int i = 0; i < s.Length; i++) {
            if ((!hashTable.ContainsKey(s[i]) && seen.Contains(t[i])) || (hashTable.ContainsKey(s[i]) && t[i] != hashTable[s[i]])) {
                return false;
            }
            hashTable[s[i]] = t[i];
            seen.Add(t[i]);
        }
        return true;
    }
}

// @lc code=end

