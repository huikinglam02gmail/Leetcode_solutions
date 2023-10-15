/*
 * @lc app=leetcode id=1944 lang=csharp
 *
 * [1944] Number of Visible People in a Queue
 */

// @lc code=start
/**
 * @lc app=leetcode id=1944 lang=csharp
 *
 * [1944] Number of Visible People in a Queue
 */

using System;
using System.Collections.Generic;

public class Solution {
    public int[] CanSeePersonsCount(int[] heights) {
        Stack<int> stack = new Stack<int>();
        int n = heights.Length;
        int[] result = new int[n];

        for (int i = n - 1; i >= 0; i--) {
            while (stack.Count > 0 && heights[i] >= heights[stack.Peek()]) {
                stack.Pop();
                result[i]++;
            }

            if (stack.Count > 0) {
                result[i]++;
            }

            stack.Push(i);
        }

        return result;
    }
}

// @lc code=end

