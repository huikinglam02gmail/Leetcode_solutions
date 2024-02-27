/*
 * @lc app=leetcode id=3005 lang=csharp
 *
 * [3005] Count Elements With Maximum Frequency
 */

// @lc code=start
using System.Collections.Generic;

public class Solution {
    public int MaxFrequencyElements(int[] nums) {
        Dictionary<int, int> hashTable = new Dictionary<int, int>();
        foreach (int num in nums) {
            if (hashTable.ContainsKey(num)) {
                hashTable[num]++;
            } else {
                hashTable[num] = 1;
            }
        }
        
        int maxOccur = 0;
        int result = 0;
        foreach (var entry in hashTable) {
            if (entry.Value > maxOccur) {
                maxOccur = entry.Value;
                result = 0;
            }
            if (entry.Value == maxOccur) {
                result += entry.Value;
            }
        }
        
        return result;
    }
}

// @lc code=end

