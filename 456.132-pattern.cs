/*
 * @lc app=leetcode id=456 lang=csharp
 *
 * [456] 132 Pattern
 */

// @lc code=start
using System;
using System.Collections.Generic;

public class Solution {
    public bool Find132pattern(int[] nums) {
        Stack<Tuple<int, int>> stack = new Stack<Tuple<int, int>>();
        foreach (int num in nums) {
            int thisMin = num;
            if (stack.Count > 0) {
                thisMin = Math.Min(thisMin, stack.Peek().Item2);
            }
            while (stack.Count > 0 && num >= stack.Peek().Item1) {
                stack.Pop();
            }
            if (stack.Count > 0 && stack.Peek().Item2 < num) {
                return true;
            }
            stack.Push(new Tuple<int, int>(num, thisMin));
        }
        return false;
    }
}

// @lc code=end

