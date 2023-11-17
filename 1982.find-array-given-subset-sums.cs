/*
 * @lc app=leetcode id=1982 lang=csharp
 *
 * [1982] Find Array Given Subset Sums
 */

// @lc code=start
using System;
using System.Collections.Generic;

public class Solution {
    public int[] RecoverArray(int n, int[] sums) {
        if (n == 0) {
            return new int[] { };
        } else {
            Array.Sort(sums);
            int x = sums[1] - sums[0];
            List<int> left = new List<int>();
            List<int> right = new List<int>();
            int indLeft = 0;

            foreach (int s in sums) {
                if (0 <= indLeft && indLeft < left.Count && s - x == left[indLeft]) {
                    right.Add(s);
                    indLeft++;
                } else {
                    left.Add(s);
                }
            }

            List<int> result;
            if (left.Contains(0)) {
                result = new List<int> {x};
                int[] leftResult = RecoverArray(n - 1, left.ToArray());
                foreach (int nxt in leftResult) result.Add(nxt);
            } else {
                result = new List<int> {- x};
                int[] rightResult = RecoverArray(n - 1, right.ToArray());
                foreach (int nxt in rightResult) result.Add(nxt);
            }
            return result.ToArray();
        }
    }
}

// @lc code=end

