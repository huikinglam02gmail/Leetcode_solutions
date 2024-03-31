/*
 * @lc app=leetcode id=2444 lang=cpp
 *
 * [2444] Count Subarrays With Fixed Bounds
 */

// @lc code=start
#include <vector>
#include <algorithm>

class Solution {
public:
    /*
    For each index i, consider all the subarrays from j <= i. We want the subarrays that exclude nums[j] < minK and nums[j] > maxK.
    Therefore we keep a record of the latest of such indices jBad. In addition, we record the last appearance of jMin: nums[jMin] = minK, and jMax: nums[jMax] = maxK.
    Once we have these three, we add max(0, min(jMin, jMax) - jBad) to the result.
    */
    long long countSubarrays(std::vector<int>& nums, int minK, int maxK) {
        int jMax = -1, jMin = -1, jBad = -1;
        long long result = 0;
        for (int j = 0; j < nums.size(); ++j) {
            int num = nums[j];
            if (num < minK || num > maxK) {
                jBad = j;
            }
            if (num == minK) {
                jMin = j;
            }
            if (num == maxK) {
                jMax = j;
            }
            result += std::max(0, std::min(jMin, jMax) - jBad);
        }
        return result;
    }
};

// @lc code=end

