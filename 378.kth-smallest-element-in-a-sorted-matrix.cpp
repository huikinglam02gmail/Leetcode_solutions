/*
 * @lc app=leetcode id=378 lang=cpp
 *
 * [378] Kth Smallest Element in a Sorted Matrix
 */

// @lc code=start
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    /*
    Binary search-based solution
    Since the matrix is sorted in both directions, we can binary search on the number of elements less than or equal to mid
    */
    int kthSmallest(vector<vector<int>>& matrix, int k) {
        int n = matrix.size();
        int left = matrix[0][0], right = matrix[n - 1][n - 1];
        while (left < right) {
            int mid = left + (right - left) / 2;
            int count = 0;
            for (const auto& row : matrix) {
                count += upper_bound(row.begin(), row.end(), mid) - row.begin();
            }
            if (count >= k) {
                right = mid;
            } else {
                left = mid + 1;
            }
        }
        return left;
    }
};

// @lc code=end

