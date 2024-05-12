/*
 * @lc app=leetcode id=378 lang=csharp
 *
 * [378] Kth Smallest Element in a Sorted Matrix
 */

// @lc code=start
using System;
using System.Collections.Generic;

public class Solution {
    /*
    Binary search-based solution
    Since the matrix is sorted in both directions, we can binary search on the number of elements less than or equal to mid
    */
    public int KthSmallest(int[][] matrix, int k) {
        int n = matrix.Length;
        int left = matrix[0][0], right = matrix[n - 1][n - 1];
        while (left < right) {
            int mid = left + (right - left) / 2;
            int count = 0;
            foreach (var row in matrix) {
                count += CountElementsLessThanOrEqualTo(row, mid);
            }
            if (count >= k) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }
        return left;
    }

    private int CountElementsLessThanOrEqualTo(int[] row, int target) {
        int left = 0, right = row.Length - 1;
        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (row[mid] <= target) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }
        return left;
    }
}

// @lc code=end

