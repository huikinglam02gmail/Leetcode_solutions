/*
 * @lc app=leetcode id=3046 lang=csharp
 *
 * [3046] Split the Array
 */

// @lc code=start
using System.Collections.Generic;

public class Solution {
    public bool IsPossibleToSplit(int[] nums) {
        Dictionary<int, int> occur = new Dictionary<int, int>();
        foreach (int num in nums) {
            if (!occur.ContainsKey(num)) {
                occur[num] = 0;
            }
            occur[num]++;
            if (occur[num] > 2) {
                return false;
            }
        }
        return true;
    }
}

// @lc code=end

