/*
 * @lc app=leetcode id=1927 lang=csharp
 *
 * [1927] Sum Game
 */

// @lc code=start
using System;
using System.Collections.Generic;

public class Solution {
    private Dictionary<Tuple<int, int, int>, bool> memo;

    public bool SumGame(string num) 
    {
        memo = new Dictionary<Tuple<int, int, int>, bool>();
        int n = num.Length;
        int l = 0;
        int r = 0;
        int leftSum = 0;
        int rightSum = 0;

        for (int i = 0; i < n; i++) {
            char c = num[i];
            if (i < n / 2) {
                if (c == '?') {
                    l++;
                } else {
                    leftSum += (c - '0');
                }
            } else {
                if (c == '?') {
                    r++;
                } else {
                    rightSum += (c - '0');
                }
            }
        }

        return DP(l - r, leftSum - rightSum, 0);
    }

    private bool DP(int diff, int lrDiff, int turn) {
        if (diff == 1) 
        {
            return (turn == 0) ? true : !(-9 <= lrDiff && lrDiff <= 0);
        } 
        else if (diff == -1) 
        {
            return (turn == 0) ? true : !(0 <= lrDiff && lrDiff <= 9);
        }
        Tuple<int, int, int> t = new Tuple<int, int, int>(diff, lrDiff, turn);
        if (!memo.ContainsKey(t))
        {
            bool result = (turn == 0) ? false : true;
            
            if (diff > 0) {
                for (int j = 0; j < 10; j++) {
                    if (turn == 0) {
                        result = result || DP(diff - 1, lrDiff + j, 1 - turn);
                    } else {
                        result = result && DP(diff - 1, lrDiff + j, 1 - turn);
                    }
                }
            } else {
                for (int j = 0; j < 10; j++) {
                    if (turn == 0) {
                        result = result || DP(diff + 1, lrDiff - j, 1 - turn);
                    } else {
                        result = result && DP(diff + 1, lrDiff - j, 1 - turn);
                    }
                }
            }
            memo.Add(t, result);
        }
        return memo[t];
    }
}

// @lc code=end

