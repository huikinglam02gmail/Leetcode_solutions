/*
 * @lc app=leetcode id=74 lang=csharp
 *
 * [74] Search a 2D Matrix
 */

// @lc code=start
using System;

public class Solution {
    public bool SearchMatrix(int[][] matrix, int target) {
        int row = 0;
        int col = matrix[0].Length - 1;
        
        while (row >= 0 && row < matrix.Length && col >= 0 && col < matrix[0].Length) {
            if (matrix[row][col] < target) {
                row++;
            } else if (matrix[row][col] > target) {
                col--;
            } else {
                return true;
            }
        }
        
        return false;
    }
}

// @lc code=end

