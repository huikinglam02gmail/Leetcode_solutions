/*
 * @lc app=leetcode id=135 lang=csharp
 *
 * [135] Candy
 */

// @lc code=start
using System;
using System.Collections.Generic;

public class Solution {
    public int Candy(int[] ratings) {
        int n = ratings.Length;
        int[] result = new int[n];
        
        for (int i = 0; i < n; i++) {
            result[i] = 1;
        }
        
        for (int i = 0; i < n - 1; i++) {
            if (ratings[i + 1] > ratings[i] && result[i + 1] <= result[i]) {
                result[i + 1] = result[i] + 1;
            }
        }
        
        for (int i = n - 1; i > 0; i--) {
            if (ratings[i] < ratings[i - 1] && result[i] >= result[i - 1]) {
                result[i - 1] = result[i] + 1;
            }
        }
        
        int sum = 0;
        foreach (int candyCount in result) {
            sum += candyCount;
        }
        
        return sum;
    }
}

// @lc code=end

