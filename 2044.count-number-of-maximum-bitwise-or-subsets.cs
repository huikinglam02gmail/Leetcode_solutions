/*
 * @lc app=leetcode id=2044 lang=csharp
 *
 * [2044] Count Number of Maximum Bitwise-OR Subsets
 */

// @lc code=start
using System;
using System.Collections.Generic;

public class Solution {
    public int CountMaxOrSubsets(int[] nums) {
        int n = nums.Length;
        int[] subSetMask = new int[1 << n];
        int i = 0;
        Dictionary<int, int> hashTable = new Dictionary<int, int>();

        for (int mask = 1; mask < (1 << n); mask++) {
            while (mask >= (1 << i)) {
                i++;
            }
            subSetMask[mask] = nums[i - 1] | subSetMask[mask - (1 << (i - 1))];
            hashTable[subSetMask[mask]] = hashTable.GetValueOrDefault(subSetMask[mask], 0) + 1;
        }

        return hashTable[GetMaxKey(hashTable)];
    }

    private int GetMaxKey(Dictionary<int, int> hashTable) {
        int maxKey = Int32.MinValue;
        foreach (var key in hashTable.Keys) {
            maxKey = Math.Max(maxKey, key);
        }
        return maxKey;
    }
}

// @lc code=end

