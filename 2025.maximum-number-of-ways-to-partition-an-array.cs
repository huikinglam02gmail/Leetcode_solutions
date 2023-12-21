/*
 * @lc app=leetcode id=2025 lang=csharp
 *
 * [2025] Maximum Number of Ways to Partition an Array
 */

// @lc code=start
using System;
using System.Collections.Generic;

public class Solution {
    public int WaysToPartition(int[] nums, int k) {
        int n = nums.Length;
        int result = 0;
        long[] prefixSum = new long[n];
        long[] suffixSum = new long[n];

        for (int i = 0; i < n; i++) {
            prefixSum[i] = nums[i];
            suffixSum[i] = nums[i];
        }

        for (int i = 1; i < n; i++) {
            prefixSum[i] += prefixSum[i - 1];
        }

        Dictionary<long, Queue<int>> left = new Dictionary<long, Queue<int>>();
        Dictionary<long, Queue<int>> right = new Dictionary<long, Queue<int>>();
        for (int i = n - 2; i >= 0; i--) {
            suffixSum[i] += suffixSum[i + 1];
            if (suffixSum[i + 1] == prefixSum[i]) result += 1;
            long diff = prefixSum[i] - suffixSum[i + 1];
            if (!right.ContainsKey(diff)) right[diff] = new Queue<int>();
            right[diff].Enqueue(i);
        }
        for (int i = 0; i < n; i++) {
            int current = (left.ContainsKey(k - nums[i]) ? left[k - nums[i]].Count : 0) +
                          (right.ContainsKey(nums[i] - k) ? right[nums[i] - k].Count : 0);

            result = Math.Max(result, current);

            if (i < n - 1) {
                long diff = prefixSum[i] - suffixSum[i + 1];
                right[diff].Dequeue();
                if (!left.ContainsKey(diff)) left[diff] = new Queue<int>();
                left[diff].Enqueue(i);
            }
        }

        return result;
    }
}

// @lc code=end

