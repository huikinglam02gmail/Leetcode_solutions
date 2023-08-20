/*
 * @lc app=leetcode id=1862 lang=csharp
 *
 * [1862] Sum of Floored Pairs
 */

// @lc code=start
using System;
using System.Collections.Generic;

public class Solution {
    public int SumOfFlooredPairs(int[] nums) {
        Dictionary<int, int> hashTable = new Dictionary<int, int>();
        
        foreach (int num in nums) {
            if (hashTable.ContainsKey(num)) {
                hashTable[num]++;
            } else {
                hashTable[num] = 1;
            }
        }
        
        int[] increment = new int[hashTable.Keys.Max()];
        
        foreach (int key in hashTable.Keys) {
            for (int j = key; j <= increment.Length; j += key) {
                increment[j - 1] += hashTable[key];
            }
        }
        
        List<long> prefixSum = new List<long> { 0 };
        
        foreach (int inc in increment) {
            prefixSum.Add(prefixSum[prefixSum.Count - 1] + inc);
        }
        
        long result = 0;
        long MOD = 1000000007;
        
        foreach (int key in hashTable.Keys) {
            result += Convert.ToInt64(hashTable[key]) * prefixSum[key];
            result %= MOD;
        }
        
        return Convert.ToInt32(result);
    }
}

// @lc code=end

