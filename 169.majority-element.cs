/*
 * @lc app=leetcode id=169 lang=csharp
 *
 * [169] Majority Element
 */

// @lc code=start
using System;
using System.Collections.Generic;

public class Solution {
    public int MajorityElement(int[] nums) {
        int candidate = -1;
        int votes = 0;
        
        foreach (int num in nums) {
            if (votes == 0) {
                candidate = num;
                votes = 1;
            } else {
                if (num == candidate) {
                    votes++;
                } else {
                    votes--;
                }
            }
        }
        
        return candidate;
    }
}

// @lc code=end

