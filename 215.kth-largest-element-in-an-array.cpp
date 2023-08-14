/*
 * @lc app=leetcode id=215 lang=cpp
 *
 * [215] Kth Largest Element in an Array
 */

// @lc code=start
#include <iostream>
#include <vector>
#include <cstdlib>
#include <ctime>

class Solution {
public:
    /*
    QuickSelect algorithm
    */
    int findKthLargest(std::vector<int>& nums, int k) {
        std::srand(std::time(0));
        int pivot = nums[std::rand() % nums.size()];
        std::vector<int> left, mid, right;

        for (int x : nums) {
            if (x > pivot) {
                left.push_back(x);
            } else if (x == pivot) {
                mid.push_back(x);
            } else {
                right.push_back(x);
            }
        }

        int L = left.size();
        int M = mid.size();

        if (k <= L) {
            return findKthLargest(left, k);
        } else if (k > L + M) {
            return findKthLargest(right, k - L - M);
        } else {
            return mid[0];
        }
    }
};

// @lc code=end

