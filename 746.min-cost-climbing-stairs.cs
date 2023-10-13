/*
 * @lc app=leetcode id=746 lang=csharp
 *
 * [746] Min Cost Climbing Stairs
 */

// @lc code=start
/**
 * @lc app=leetcode id=746 lang=csharp
 *
 * [746] Min Cost Climbing Stairs
 */

public class Solution {
    /*
    DP question clearly
    dp[i] = min cost to reach i
    0 and 1 are trivial    
    */
    public int MinCostClimbingStairs(int[] cost) {
        int a = 0, b = 0;
        int n = cost.Length;

        for (int i = 0; i < n; i++) {
            int temp = a;
            a = b;
            b = Math.Min(temp, b) + cost[i];
        }

        return Math.Min(a, b);
    }
}

// @lc code=end

