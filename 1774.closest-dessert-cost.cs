/*
 * @lc app=leetcode id=1774 lang=csharp
 *
 * [1774] Closest Dessert Cost
 */

// @lc code=start
using System;

public class Solution {
    private int[] baseCosts;
    private int[] toppingCosts;
    private int target;
    private int result;
    private int resultDiff;

    public int ClosestCost(int[] baseCosts, int[] toppingCosts, int target) {
        this.baseCosts = baseCosts;
        this.toppingCosts = toppingCosts;
        this.target = target;
        this.result = -1;
        this.resultDiff = int.MaxValue;

        for (int i = 0; i < baseCosts.Length; i++) {
            Backtracking(0, baseCosts[i] - target);
        }

        return result;
    }

    private void Backtracking(int i, int diff) {
        if ((diff > 0 && Math.Abs(diff) < resultDiff) || (diff <= 0 && Math.Abs(diff) <= resultDiff)) {
            result = target + diff;
            resultDiff = Math.Abs(diff);
        }

        if (diff < 0 && i < toppingCosts.Length) {
            for (int j = 0; j < 3; j++) {
                Backtracking(i + 1, diff + j * toppingCosts[i]);
            }
        }
    }
}

// @lc code=end

