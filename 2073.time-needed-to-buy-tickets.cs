/*
 * @lc app=leetcode id=2073 lang=csharp
 *
 * [2073] Time Needed to Buy Tickets
 */

// @lc code=start
using System;
using System.Collections.Generic;

public class Solution {
    public int TimeRequiredToBuy(int[] tickets, int k) {
        int result = 0;
        while (tickets[k] > 0) {
            for (int i = 0; i < tickets.Length; i++) {
                if (tickets[i] > 0) {
                    result++;
                    tickets[i]--;
                }
                if (i == k && tickets[i] == 0) {
                    return result;
                }
            }
        }
        return -1;
    }
}

// @lc code=end

