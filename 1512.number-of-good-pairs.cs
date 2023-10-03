/*
 * @lc app=leetcode id=1512 lang=csharp
 *
 * [1512] Number of Good Pairs
 */

// @lc code=start
using System;
using System.Collections.Generic;

public class Solution {
    public int NumIdenticalPairs(int[] nums) {
        Dictionary<int, int> hashTable = new Dictionary<int, int>();

        foreach (int num in nums) {
            if (hashTable.ContainsKey(num)) {
                hashTable[num]++;
            } else {
                hashTable[num] = 1;
            }
        }

        int result = 0;

        foreach (var kvp in hashTable) {
            int count = kvp.Value;
            result += count * (count - 1) / 2;
        }

        return result;
    }
}

// @lc code=end

