/*
 * @lc app=leetcode id=503 lang=csharp
 *
 * [503] Next Greater Element II
 */

// @lc code=start
/**
 * @lc app=leetcode id=503 lang=csharp
 *
 * [503] Next Greater Element II
 */

using System;
using System.Collections.Generic;

public class Solution {
    public int[] NextGreaterElements(int[] nums) {
        int n = nums.Length;
        int[] nextGreater = new int[2 * n];
        Array.Fill(nextGreater, -1);
        Stack<int> stack = new Stack<int>();
        int[] nums2 = new int[n * 2];

        for (int i = 0; i < n; i++) {
            nums2[i] = nums[i];
            nums2[i + n] = nums[i];
        }

        for (int i = 0; i < n * 2; i++) {
            while (stack.Count > 0 && nums2[i] > nums2[stack.Peek()]) {
                nextGreater[stack.Pop()] = nums2[i];
            }
            stack.Push(i);
        }

        return nextGreater.Take(n).ToArray();
    }
}

// @lc code=end

