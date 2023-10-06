/*
 * @lc app=leetcode id=1931 lang=csharp
 *
 * [1931] Painting a Grid With Three Different Colors
 */

// @lc code=start
using System;
using System.Collections.Generic;

public class Solution {
    public bool StatesAreCompatible(int state1, int state2) {
        while (state1 > 0 && state2 > 0) {
            if (state1 % (1 << 3) == state2 % (1 << 3)) {
                return false;
            }
            state1 >>= 3;
            state2 >>= 3;
        }
        return true;
    }

    public int ColorTheGrid(int m, int n) {
        int MOD = (int)Math.Pow(10, 9) + 7;
        Queue<int> dq = new Queue<int>();
        int steps = 0;
        dq.Enqueue(0);

        while (dq.Count > 0 && steps < m) {
            int dqCount = dq.Count;
            for (int i = 0; i < dqCount; i++) {
                int state = dq.Dequeue();
                int newState = state << 3;
                for (int j = 0; j < 3; j++) {
                    if ((state % (1 << 3)) != (1 << j)) {
                        dq.Enqueue(newState ^ (1 << j));
                    }
                }
            }
            steps++;
        }

        if (n == 1) {
            return dq.Count;
        }

        List<int> possibleStates = new List<int>(dq);

        Dictionary<int, HashSet<int>> currentToPrevMap = new Dictionary<int, HashSet<int>>();
        foreach (int key in possibleStates) {
            currentToPrevMap[key] = new HashSet<int>();
            foreach (int key1 in possibleStates) {
                if (StatesAreCompatible(key, key1)) {
                    currentToPrevMap[key].Add(key1);
                }
            }
        }

        Dictionary<int, int> dp = new Dictionary<int, int>();
        foreach (int key in possibleStates) {
            dp[key] = 1;
        }

        for (int j = 1; j < n; j++) {
            Dictionary<int, int> dpNew = new Dictionary<int, int>();
            foreach (int key in currentToPrevMap.Keys) {
                dpNew[key] = 0;
                foreach (int oldKey in currentToPrevMap[key]) {
                    dpNew[key] = (dpNew[key] + dp[oldKey]) % MOD;
                }
            }
            dp = dpNew;
        }

        int result = 0;
        foreach (int key in dp.Keys) {
            result = (result + dp[key]) % MOD;
        }
        return result;
    }
}

// @lc code=end

