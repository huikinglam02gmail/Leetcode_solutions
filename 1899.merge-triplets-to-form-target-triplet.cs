/*
 * @lc app=leetcode id=1899 lang=csharp
 *
 * [1899] Merge Triplets to Form Target Triplet
 */

// @lc code=start
using System;
using System.Collections.Generic;

public class Solution {
    public bool MergeTriplets(int[][] triplets, int[] target) {
        int[] satisfy = new int[3];

        for (int i = 0; i < triplets.Length; i++) {
            if (triplets[i][0] <= target[0] && triplets[i][1] <= target[1] && triplets[i][2] <= target[2]) {
                satisfy[0] = Math.Max(satisfy[0], triplets[i][0]);
                satisfy[1] = Math.Max(satisfy[1], triplets[i][1]);
                satisfy[2] = Math.Max(satisfy[2], triplets[i][2]);
            }
        }

        return satisfy[0] == target[0] && satisfy[1] == target[1] && satisfy[2] == target[2];
    }
}

// @lc code=end

