/*
 * @lc app=leetcode id=1818 lang=cpp
 *
 * [1818] Minimum Absolute Sum Difference
 */

// @lc code=start
#include <iostream>
#include <vector>
#include <algorithm>

using std::abs;
using std::lower_bound;
using std::max;
using std::min;
using std::sort;
using std::vector;

class Solution {
public:
    int minAbsoluteSumDiff(vector<int>& nums1, vector<int>& nums2) {
        const int MOD = 1000000007;
        vector<int> nums1Sorted = nums1;
        sort(nums1Sorted.begin(), nums1Sorted.end());

        long long result = 0;
        long long maxGain = 0;
        for (size_t i = 0; i < nums2.size(); i++) {
            int num = nums2[i];
            int gain = abs(nums1[i] - num);
            result += (long long)gain;
            int indLeft = lower_bound(nums1Sorted.begin(), nums1Sorted.end(), num) - nums1Sorted.begin();
            if (indLeft > 0 && indLeft <= nums1Sorted.size())
                gain = min(gain, abs(nums1Sorted[indLeft - 1] - num));
            if (indLeft >= 0 && indLeft < nums1Sorted.size())
                gain = min(gain, abs(nums1Sorted[indLeft] - num));
            maxGain = max(maxGain, static_cast<long long>(abs(nums1[i] - num) - gain));
        }

        result = (result - maxGain + MOD) % MOD;
        return static_cast<int>(result);
    }
};

// @lc code=end

