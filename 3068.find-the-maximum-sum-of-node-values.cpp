/*
 * @lc app=leetcode id=3068 lang=cpp
 *
 * [3068] Find the Maximum Sum of Node Values
 */

// @lc code=start
#include <vector>
#include <algorithm>
#include <cmath>
#include <climits>

class Solution {
public:
    /*
    As the graph is a tree, we can always flip an even number of nodes (no need to care about the edges) to get a larger sum.
    That is, if count(num ^ k > num for num in nums) is even, we can return the maximum sum possible.
    For the case in which this count is odd, we have to reduce the maxSum by min(abs(num ^ k - num)), which points to the node in which num is closest to num ^ k. For example, in example 2, nums = [7, 3], k = 7, maxSum is 7 + 4 = 11, and count = 1. As count is odd, the maxSum has included a flip that violated the rule. We can choose the one which induced the least change, which is flip of 3 to 4.
    */
    long long maximumValueSum(std::vector<int>& nums, int k, std::vector<std::vector<int>>& edges) {
        int count = 0;
        long long maxSum = 0;
        int sacrifice = INT_MAX;

        for (int num : nums) {
            if ((num ^ k) > num) count++;
            sacrifice = std::min(sacrifice, std::abs((num ^ k) - num));
            maxSum += std::max(num, num ^ k);
        }

        if (count % 2 != 0) maxSum -= sacrifice;

        return maxSum;
    }
};

// @lc code=end

