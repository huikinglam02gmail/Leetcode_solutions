/*
 * @lc app=leetcode id=1850 lang=csharp
 *
 * [1850] Minimum Adjacent Swaps to Reach the Kth Smallest Number
 */

// @lc code=start
using System;
using System.Collections.Generic;

public class Solution {
    public void NextPermutation(List<int> nums) {
        int n = nums.Count;
        int i = n - 2;
        while (i >= 0 && nums[i] >= nums[i + 1]) {
            i--;
        }
        if (i >= 0) {
            int j = n - 1;
            while (j > i && nums[i] >= nums[j]) {
                j--;
            }
            int temp = nums[i];
            nums[i] = nums[j];
            nums[j] = temp;
        }

        i++;
        int end = n - 1;
        while (i < end) {
            int temp = nums[i];
            nums[i] = nums[end];
            nums[end] = temp;
            i++;
            end--;
        }
    }

    public int GetMinSwaps(string num, int k) {
        List<int> target = new List<int>();
        foreach (char c in num) {
            target.Add((int)Char.GetNumericValue(c));
        }
        for (int i = 0; i < k; i++) {
            NextPermutation(target);
        }
        List<int> original = new List<int>();
        foreach (char c in num) {
            original.Add((int)Char.GetNumericValue(c));
        }
        int result = 0;
        int n = original.Count;
        for (int i = 0; i < n; i++) {
            int j = i;
            while (original[j] != target[i]) {
                j++;
            }
            while (j > i) {
                int temp = original[j];
                original[j] = original[j - 1];
                original[j - 1] = temp;
                j--;
                result++;
            }
        }
        return result;
    }
}

// @lc code=end

