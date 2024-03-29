/*
 * @lc app=leetcode id=2962 lang=csharp
 *
 * [2962] Count Subarrays Where Max Element Appears at Least K Times
 */

// @lc code=start
using System;
using System.Collections.Generic;

public class Solution {
    public long CountSubarrays(int[] nums, int k) {
        int maxNum = nums[0];
        foreach (int num in nums) {
            maxNum = Math.Max(maxNum, num);
        }
        
        List<int> appear = new List<int>();
        long result = 0;
        for (int i = 0; i < nums.Length; i++) {
            if (nums[i] == maxNum) {
                appear.Add(i);
            }
        }
        
        for (int i = 0; i < nums.Length; i++) {
            int index = BinarySearchRight(appear, i);
            if (index >= k) {
                result += appear[index - k] + 1;
            }
        }
        
        return result;
    }
    
    private int BinarySearchRight(List<int> appear, int target) {
        int left = 0;
        int right = appear.Count;
        while (left < right) {
            int mid = left + (right - left) / 2;
            if (appear[mid] <= target) {
                left = mid + 1;
            } else {
                right = mid;
            }
        }
        return left;
    }
}

// @lc code=end

