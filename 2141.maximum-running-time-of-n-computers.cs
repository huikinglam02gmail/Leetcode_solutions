/*
 * @lc app=leetcode id=2141 lang=csharp
 *
 * [2141] Maximum Running Time of N Computers
 */

// @lc code=start
using System;
using System.Collections.Generic;

public class Solution {
    public long MaxRunTime(int n, int[] batteries) {
        Array.Sort(batteries);
        long S = batteries.Select(x => (long)x).Sum();
        int j = batteries.Length - 1;
        while (batteries[j] > S / n) {
            n--;
            S -= (long)batteries[j];
            j--;
        }
        return S / n;        
    }
}

// @lc code=end

