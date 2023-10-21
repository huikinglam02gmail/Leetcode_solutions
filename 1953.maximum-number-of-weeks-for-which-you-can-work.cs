/*
 * @lc app=leetcode id=1953 lang=csharp
 *
 * [1953] Maximum Number of Weeks for Which You Can Work
 */

// @lc code=start
using System;

public class Solution {
    public long NumberOfWeeks(int[] milestones) {
        long M = 0;
        long S = 0;

        foreach (long milestone in milestones) {
            M = Math.Max(M, milestone);
            S += milestone;
        }

        return 2 * M <= S ? S : 2 * (S - M) + 1;
    }
}

// @lc code=end

