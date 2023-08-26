/*
 * @lc app=leetcode id=1872 lang=csharp
 *
 * [1872] Stone Game VIII
 */

// @lc code=start
using System;
using System.Collections.Generic;

public class Solution {
    public int StoneGameVIII(int[] stones) {
        int dp = 0;
        int total = 0;
        int n = stones.Length;
        
        for (int i = 0; i < n; i++) {
            total += stones[i];
        }
        
        dp = total;
        
        for (int i = n - 2; i > 0; i--) {
            total -= stones[i + 1];
            dp = Math.Max(dp, total - dp);
        }
        
        return dp;
    }
}

// @lc code=end

