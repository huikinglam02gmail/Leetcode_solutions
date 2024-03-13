/*
 * @lc app=leetcode id=2064 lang=csharp
 *
 * [2064] Minimized Maximum of Products Distributed to Any Store
 */

// @lc code=start
using System;
using System.Collections.Generic;

public class Solution {
    public int MinimizedMaximum(int n, int[] quantities) {
        int l = 1, r = quantities.Max();
        while (l < r) {
            int mid = l + (r - l) / 2;
            int numPeople = 0;
            foreach (int q in quantities) {
                numPeople += CeilDiv(q, mid);
            }
            if (numPeople <= n) {
                r = mid;
            } else {
                l = mid + 1;
            }
        }
        return l;
    }
    
    private int CeilDiv(int a, int b) {
        return (a + b - 1) / b;
    }
}

// @lc code=end

