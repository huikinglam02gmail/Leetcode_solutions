/*
 * @lc app=leetcode id=1356 lang=csharp
 *
 * [1356] Sort Integers by The Number of 1 Bits
 */

// @lc code=start
using System;
using System.Linq;
using System.Collections.Generic;

public class Solution {
    public int[] SortByBits(int[] arr) {
        return arr.OrderBy(num => CountBits(num)).ThenBy(num => num).ToArray();
    }

    private int CountBits(int num) {
        int count = 0;
        while (num > 0) {
            count += num & 1;
            num >>= 1;
        }
        return count;
    }
}

// @lc code=end

