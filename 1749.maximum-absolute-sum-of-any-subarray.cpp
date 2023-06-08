/*
 * @lc app=leetcode id=1749 lang=cpp
 *
 * [1749] Maximum Absolute Sum of Any Subarray
 */

// @lc code=start
#include <vector>;
#include <algorithm>;
#include <cmath>;
using std::abs;
using std::max;
using std::min;
using std::vector;

class Solution 
{
public:
    int MaxSubArray(vector<int>& nums)
    {
        int maxSoFar = INT_MIN;
        int maxEndingHere = 0;
        for (int&  num : nums)
        {
            maxEndingHere += num;
            maxSoFar = max(maxSoFar, maxEndingHere);
            maxEndingHere = max(0, maxEndingHere);
        }
        return maxSoFar;
    }

    int MinSubArray(vector<int>& nums)
    {
        int minSoFar = INT_MAX;
        int minEndingHere = 0;
        for (int&  num : nums)
        {
            minEndingHere += num;
            minSoFar = min(minSoFar, minEndingHere);
            minEndingHere = min(0, minEndingHere);
        }
        return minSoFar;
    }

    int maxAbsoluteSum(vector<int>& nums) 
    {
        return max(abs(MaxSubArray(nums)), abs(MinSubArray(nums)));
    }
};
// @lc code=end

