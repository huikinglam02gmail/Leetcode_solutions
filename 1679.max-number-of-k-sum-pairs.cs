/*
 * @lc app=leetcode id=1679 lang=csharp
 *
 * [1679] Max Number of K-Sum Pairs
 */

// @lc code=start
using System.Collections.Generic;
using System;
public class Solution 
{
    public int MaxOperations(int[] nums, int k) 
    {
        Dictionary<int, int> hashTable = new Dictionary<int, int>();
        foreach (int num in nums)
        {
            if (!hashTable.ContainsKey(num))
            {
                hashTable[num] = 0;
            }
            hashTable[num]++;
        }
        
        int result = 0;
        foreach (int key in hashTable.Keys)
        {
            if (k == 2 * key)
            {
                result += (hashTable[key] / 2 ) * 2;
            }
            else if (hashTable.ContainsKey(k - key))
            {
                result += Math.Min(hashTable[key], hashTable[k - key]);
            }
        }
        return result / 2;
    }
}
// @lc code=end

