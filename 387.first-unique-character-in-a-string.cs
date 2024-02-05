/*
 * @lc app=leetcode id=387 lang=csharp
 *
 * [387] First Unique Character in a String
 */

// @lc code=start
using System;
using System.Collections.Generic;

public class Solution {
    public int FirstUniqChar(string s) {
        List<int>[] hashTable = new List<int>[26];
        for (int i = 0; i < 26; i++) {
            hashTable[i] = new List<int>();
        }

        for (int i = 0; i < s.Length; i++) {
            char c = s[i];
            hashTable[c - 'a'].Add(i);
        }

        List<int> candidates = new List<int>();
        for (int i = 0; i < 26; i++) {
            if (hashTable[i].Count == 1) {
                candidates.Add(hashTable[i][0]);
            }
        }

        candidates.Sort();

        if (candidates.Count == 0) {
            return -1;
        } else {
            return candidates[0];
        }
    }
}

// @lc code=end

