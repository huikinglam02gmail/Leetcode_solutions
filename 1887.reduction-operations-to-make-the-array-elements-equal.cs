/*
 * @lc app=leetcode id=1887 lang=csharp
 *
 * [1887] Reduction Operations to Make the Array Elements Equal
 */

// @lc code=start
using System;
using System.Collections.Generic;
using System.Linq;

public class Solution {
    public int ReductionOperations(int[] nums) {
        Dictionary<int, int> hashTable = new Dictionary<int, int>();
        
        foreach (int num in nums) {
            if (hashTable.ContainsKey(num)) {
                hashTable[num]++;
            }
            else {
                hashTable[num] = 1;
            }
        }
        
        int result = 0;
        List<int> keys = hashTable.Keys.ToList();
        keys.Sort();
        
        int current = 0;
        int n = keys.Count;
        
        for (int i = n - 1; i > 0; i--) {
            current += hashTable[keys[i]];
            result += current;
        }
        
        return result;
    }
}

// @lc code=end

