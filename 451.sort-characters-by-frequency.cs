/*
 * @lc app=leetcode id=451 lang=csharp
 *
 * [451] Sort Characters By Frequency
 */

// @lc code=start
using System;
using System.Collections.Generic;
using System.Linq;

public class Solution {
    public string FrequencySort(string s) {
        Dictionary<char, int> hashTable = new Dictionary<char, int>();

        foreach (char c in s) {
            if (hashTable.ContainsKey(c)) {
                hashTable[c]++;
            } else {
                hashTable[c] = 1;
            }
        }

        var frequencies = hashTable.ToList();
        frequencies.Sort((x, y) => y.Value.CompareTo(x.Value));

        string result = "";
        foreach (var pair in frequencies) {
            result += new string(pair.Key, pair.Value);
        }

        return result;
    }
}

// @lc code=end

