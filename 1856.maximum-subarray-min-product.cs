/*
 * @lc app=leetcode id=1856 lang=csharp
 *
 * [1856] Maximum Subarray Min-Product
 */

// @lc code=start
using System;
using System.Collections.Generic;

public class Solution {
    public int MaxSumMinProduct(int[] nums) {
        List<long> prefix = new List<long>();
        prefix.Add(0);
        foreach (int num in nums) {
            prefix.Add(prefix.Last() + num);
        }
        
        Stack<int> stack = new Stack<int>();
        stack.Push(-1);
        List<int> Nums = nums.ToList();
        Nums.Add(-1);
        long result = 0;
        long MOD = 1000000007;
        for (int i = 0; i < Nums.Count; i++) {
            while (stack.Count > 0 && Nums[(stack.Peek() + Nums.Count) % Nums.Count] > Nums[i]) {
                result = Math.Max(result, Nums[stack.Pop()] * (prefix[i] - prefix[stack.Peek() + 1]));
            }
            stack.Push(i);
        }
        return (int)(result % MOD);
    }
}


// @lc code=end

