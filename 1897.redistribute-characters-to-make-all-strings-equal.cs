/*
 * @lc app=leetcode id=1897 lang=csharp
 *
 * [1897] Redistribute Characters to Make All Strings Equal
 */

// @lc code=start
using System;
using System.Collections.Generic;

public class Solution {
    public bool MakeEqual(string[] words) {
        int[] hashTable = new int[26];
        
        foreach (string word in words) {
            foreach (char c in word) {
                hashTable[c - 'a']++;
            }
        }
        
        foreach (int count in hashTable) {
            if (count % words.Length != 0) {
                return false;
            }
        }
        
        return true;
    }
}

// @lc code=end

