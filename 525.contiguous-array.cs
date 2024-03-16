/*
 * @lc app=leetcode id=525 lang=csharp
 *
 * [525] Contiguous Array
 */

// @lc code=start
using System;
using System.Collections.Generic;

public class Solution {
    public int FindMaxLength(int[] nums) {
        Dictionary<int, int[]> hashTable = new Dictionary<int, int[]>();
        hashTable.Add(0, new int[] { -1, -1 });
        int total = 0;
        int result = 0;
        for (int i = 0; i < nums.Length; i++) {
            if (nums[i] == 0) total--;
            else total++;
            
            if (!hashTable.ContainsKey(total)) {
                hashTable.Add(total, new int[] { i, i });
            } else {
                int[] indexes = hashTable[total];
                indexes[1] = i;
                hashTable[total] = indexes;
            }
        }
        
        foreach (var key in hashTable.Keys) {
            result = Math.Max(result, hashTable[key][1] - hashTable[key][0]);
        }
        
        return result;
    }
}

// @lc code=end

