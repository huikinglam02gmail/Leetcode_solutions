/*
 * @lc app=leetcode id=791 lang=csharp
 *
 * [791] Custom Sort String
 */

// @lc code=start
using System.Collections.Generic;

public class Solution {
    public string CustomSortString(string order, string s) {
        Dictionary<char, int> hashTable = new Dictionary<char, int>();
        string rest = "";
        foreach (char c in s) {
            if (order.Contains(c)) {
                if (!hashTable.ContainsKey(c)) {
                    hashTable[c] = 0;
                }
                hashTable[c]++;
            } else {
                rest += c;
            }
        }
        string result = "";
        foreach (char c in order) {
            if (hashTable.ContainsKey(c)) {
                for (int j = 0; j < hashTable[c]; j++) {
                    result += c;
                }
            }
        }
        result += rest;
        return result;
    }
}

// @lc code=end

