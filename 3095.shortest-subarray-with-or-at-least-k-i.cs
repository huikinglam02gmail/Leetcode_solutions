/*
 * @lc app=leetcode id=3095 lang=csharp
 *
 * [3095] Shortest Subarray With OR at Least K I
 */

// @lc code=start
using System;
using System.Collections.Generic;

public class Solution {
    /*
    sliding window
    0 <= nums[i] <= 50: at most most 6 bits
    For each num in nums, we update current count of number of each bit. If removing the left element from the collecton would not make the subarray OR less than k, we would proceed to remove it.
    */
    private void UpdateHashTable(bool addOrRemove, int num) {
        for (int i = 0; i < 6; i++) {
            if ((num & (1 << i)) != 0) {
                if (addOrRemove) {
                    hashTable[i]++;
                } else {
                    hashTable[i]--;
                }
                if (hashTable[i] == 1 && addOrRemove) {
                    current += (1 << i);
                }
                if (hashTable[i] == 0 && !addOrRemove) {
                    current -= (1 << i);
                }
            }
        }
    }

    public int MinimumSubarrayLength(int[] nums, int k) {
        int left = 0;
        int n = nums.Length;
        current = 0;
        hashTable = new int[6];
        int result = n + 1;
        for (int right = 0; right < n; right++) {
            UpdateHashTable(true, nums[right]);
            if (current >= k) {
                result = Math.Min(result, right - left + 1);
            }
            bool cannotProceed = false;
            while (left < right && !cannotProceed) {
                UpdateHashTable(false, nums[left]);
                if (current >= k) {
                    left++;
                    result = Math.Min(result, right - left + 1);
                } else {
                    cannotProceed = true;
                    UpdateHashTable(true, nums[left]);
                }
            }
        }
        return result <= n ? result : -1;
    }

    private int[] hashTable;
    private int current;
}

// @lc code=end

