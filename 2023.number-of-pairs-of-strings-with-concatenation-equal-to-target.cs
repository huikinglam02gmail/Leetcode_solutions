/*
 * @lc app=leetcode id=2023 lang=csharp
 *
 * [2023] Number of Pairs of Strings With Concatenation Equal to Target
 */

// @lc code=startusing System;
using System.Collections.Generic;

public class Solution {
    public int NumOfPairs(string[] nums, string target) {
        int n = target.Length;
        Dictionary<string, int> hashTable = new Dictionary<string, int>();

        for (int i = 0; i < n - 1; i++) {
            string prefix = target.Substring(0, i + 1);
            if (!hashTable.ContainsKey(prefix)) {
                hashTable[prefix] = 0;
            }

            string suffix = target.Substring(i + 1);
            if (!hashTable.ContainsKey(suffix)) {
                hashTable[suffix] = 0;
            }
        }

        foreach (var num in nums) {
            if (hashTable.ContainsKey(num)) {
                hashTable[num]++;
            }
        }

        int result = 0;
        for (int i = 0; i < n - 1; i++) {
            string prefix = target.Substring(0, i + 1);
            string suffix = target.Substring(i + 1);

            if (prefix == suffix) {
                result += hashTable[prefix] * (hashTable[prefix] - 1);
            } else {
                result += hashTable[prefix] * hashTable[suffix];
            }
        }

        return result;
    }
}

// @lc code=end

