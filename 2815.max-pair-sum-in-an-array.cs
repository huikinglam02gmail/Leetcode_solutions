/*
 * @lc app=leetcode id=2815 lang=csharp
 *
 * [2815] Max Pair Sum in an Array
 */

// @lc code=start
using System;
using System.Collections.Generic;

public class Solution {
    public int MaxSum(int[] nums) {
        List<int>[] hashTable = new List<int>[10];
        for (int i = 0; i < 10; i++) {
            hashTable[i] = new List<int>();
        }
        
        foreach (int num in nums) {
            string numString = num.ToString();
            int maxDigit = 0;
            foreach (char c in numString) {
                maxDigit = Math.Max(int.Parse(c.ToString()), maxDigit);
            }
            hashTable[maxDigit].Add(num);
        }
        
        int result = -1;
        for (int i = 0; i < 10; i++) {
            if (hashTable[i].Count >= 2) {
                hashTable[i].Sort();
                result = Math.Max(result, hashTable[i][hashTable[i].Count - 1] + hashTable[i][hashTable[i].Count - 2]);
            }
        }
        
        return result;
    }
}

// @lc code=end

