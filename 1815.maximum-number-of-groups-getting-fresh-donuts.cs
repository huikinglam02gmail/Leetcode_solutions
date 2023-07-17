/*
 * @lc app=leetcode id=1815 lang=csharp
 *
 * [1815] Maximum Number of Groups Getting Fresh Donuts
 */

// @lc code=start
using System;
using System.Collections.Generic;

public class Solution {
    private Dictionary<(string, int), int> memo = new Dictionary<(string, int), int>();
    
    public int MaxHappyGroups(int batchSize, int[] groups) {
        int[] counts = new int[batchSize];
        foreach (int group in groups) {
            counts[group % batchSize]++;
        }
        int result = counts[0];
        for (int i = 1; i <= batchSize / 2; i++) {
            int toReduce = (2 * i != batchSize) ? Math.Min(counts[i], counts[batchSize - i]) : counts[i] / 2;
            counts[i] -= toReduce;
            counts[batchSize - i] -= toReduce;
            result += toReduce;
        }
        
        string initialState = "";
        for (int i = 1; i < batchSize; i++) {
            initialState += new string(i.ToString()[0], counts[i]);
        }
        return result + Dp(initialState, 0, batchSize);
    }
    
    private int Dp(string state, int remainder, int batchSize) {
        if (state.Length == 0) return 0;
        if (memo.TryGetValue((state, remainder), out int cachedValue)) {
            return cachedValue;
        }
        
        int result = (remainder == 0) ? 1 : 0;
        int extra = 0;
        
        for (int i = 0; i < state.Length; i++) {
            if (i == 0 || state[i] != state[i - 1]) {
                int nextRemainder = (remainder + (int)Char.GetNumericValue(state[i])) % batchSize;
                extra = Math.Max(extra, Dp(state.Substring(0, i) + state.Substring(i + 1), nextRemainder, batchSize));
            }
        }
        
        memo[(state, remainder)] = result + extra;
        return memo[(state, remainder)];
    }
}

// @lc code=end

