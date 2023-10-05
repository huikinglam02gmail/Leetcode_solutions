/*
 * @lc app=leetcode id=229 lang=csharp
 *
 * [229] Majority Element II
 */

// @lc code=start
using System.Collections.Generic;

public class Solution {
    public IList<int> MajorityElement(int[] nums) {
        Dictionary<int, int> hashTable = new Dictionary<int, int>();
        int n = nums.Length;
        foreach (int num in nums) {
            if (hashTable.ContainsKey(num)) {
                hashTable[num]++;
            } else {
                hashTable[num] = 1;
            }
        }
        
        List<int> result = new List<int>();
        foreach (var kvp in hashTable) {
            if (kvp.Value > n / 3) {
                result.Add(kvp.Key);
            }
        }
        
        return result;
    }
}

// @lc code=end

