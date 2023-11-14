/*
 * @lc app=leetcode id=1981 lang=csharp
 *
 * [1981] Minimize the Difference Between Target and Chosen Elements
 */

// @lc code=start
using System;
using System.Collections.Generic;

public class Solution {
    public int MinimizeTheDifference(int[][] mat, int target) {
        HashSet<int> current = new HashSet<int>();
        current.Add(0);

        foreach (int[] row in mat) {
            HashSet<int> next = new HashSet<int>();
            foreach (int r in row) {
                foreach (var s in current) {
                    next.Add(r + s);
                }
            }
            current = next;
        }

        int i = 0;
        while (target - i >= 0 || target + i <= 4900) {
            if (current.Contains(target - i) || current.Contains(target + i)) {
                return i;
            }
            else {
                i++;
            }
        }

        return -1;
    }
}

// @lc code=end

