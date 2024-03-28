/*
 * @lc app=leetcode id=2958 lang=csharp
 *
 * [2958] Length of Longest Subarray With at Most K Frequency
 */

// @lc code=start
using System;
using System.Collections.Generic;

public class Solution {
    public int MaxSubarrayLength(int[] nums, int k) {
        Dictionary<int, int> hashTable = new Dictionary<int, int>();
        int left = 0;
        int result = 0;
        for (int right = 0; right < nums.Length; right++) {
            int num = nums[right];
            while (hashTable.ContainsKey(num) && hashTable[num] == k) {
                if (hashTable.ContainsKey(nums[left])) {
                    hashTable[nums[left]]--;
                    if (hashTable[nums[left]] == 0) {
                        hashTable.Remove(nums[left]);
                    }
                }
                left++;
            }
            hashTable[num] = hashTable.GetValueOrDefault(num, 0) + 1;
            result = Math.Max(result, right - left + 1);
        }
        return result;
    }
}

// @lc code=end

