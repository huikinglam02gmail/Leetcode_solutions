/*
 * @lc app=leetcode id=661 lang=csharp
 *
 * [661] Image Smoother
 */

// @lc code=start
using System;
using System.Collections.Generic;

public class Solution {
    public int[][] ImageSmoother(int[][] img) {
        int m = img.Length;
        int n = img[0].Length;
        int[][] result = new int[m][];
        for (int i = 0; i < m; i++) {
            result[i] = new int[n];
            for (int j = 0; j < n; j++) {
                int avg = 0;
                int counter = 0;
                for (int k = -1; k <= 1; k++) {
                    for (int l = -1; l <= 1; l++) {
                        if (0 <= i + k && i + k < m && 0 <= j + l && j + l < n) {
                            avg += img[i + k][j + l];
                            counter++;
                        }
                    }
                }
                result[i][j] = avg / counter;
            }
        }
        return result;
    }
}

// @lc code=end

