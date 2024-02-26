/*
 * @lc app=leetcode id=2956 lang=csharp
 *
 * [2956] Find Common Elements Between Two Arrays
 */

// @lc code=start
using System.Collections.Generic;

public class Solution {
    public int[] FindIntersectionValues(int[] nums1, int[] nums2) {
        Dictionary<int, int> hashTable1 = new Dictionary<int, int>();
        Dictionary<int, int> hashTable2 = new Dictionary<int, int>();
        
        foreach (int num in nums1) {
            if (hashTable1.ContainsKey(num)) {
                hashTable1[num]++;
            } else {
                hashTable1[num] = 1;
            }
        }
        
        foreach (int num in nums2) {
            if (hashTable2.ContainsKey(num)) {
                hashTable2[num]++;
            } else {
                hashTable2[num] = 1;
            }
        }
        
        int[] result = new int[2];
        foreach (int key in hashTable1.Keys) {
            if (hashTable2.ContainsKey(key)) {
                result[0] += hashTable1[key];
            }
        }
        
        foreach (int key in hashTable2.Keys) {
            if (hashTable1.ContainsKey(key)) {
                result[1] += hashTable2[key];
            }
        }
        
        return result;
    }
}

// @lc code=end

