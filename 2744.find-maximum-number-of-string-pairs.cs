/*
 * @lc app=leetcode id=2744 lang=csharp
 *
 * [2744] Find Maximum Number of String Pairs
 */

// @lc code=start
using System;
using System.Collections.Generic;

public class Solution {
    public int MaximumNumberOfStringPairs(string[] words) {
        int result = 0;
        Dictionary<string, int> hashTable = new Dictionary<string, int>();

        foreach (string word in words) {
            if (hashTable.ContainsKey(word)) {
                result += hashTable[word];
            }
            string reversedWord = new string(word.Reverse().ToArray());
            hashTable[reversedWord] = hashTable.TryGetValue(reversedWord, out int count) ? count + 1 : 1;
        }

        return result;
    }
}

// @lc code=end

