/*
 * @lc app=leetcode id=2391 lang=csharp
 *
 * [2391] Minimum Amount of Time to Collect Garbage
 */

// @lc code=start
using System;
using System.Collections.Generic;

public class Solution {
    public int GarbageCollection(string[] garbage, int[] travel) {
        Dictionary<char, List<int>> hashTable = new Dictionary<char, List<int>>() {
            { 'M', new List<int>() },
            { 'P', new List<int>() },
            { 'G', new List<int>() }
        };

        for (int i = 0; i < garbage.Length; i++) {
            foreach (char c in garbage[i]) {
                hashTable[c].Add(i);
            }
        }

        List<int> prefix = new List<int> { 0 };
        foreach (int t in travel) prefix.Add(prefix.Last() + t);

        int result = 0;

        foreach (List<int> route in hashTable.Values) {
            for (int i = 0; i < route.Count; i++) {
                result += 1 + prefix[route[i]] - prefix[i == 0 ? 0 : route[i - 1]];
            }
        }

        return result;
    }
}

// @lc code=end

