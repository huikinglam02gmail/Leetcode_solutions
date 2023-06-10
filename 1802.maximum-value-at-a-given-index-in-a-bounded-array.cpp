/*
 * @lc app=leetcode id=1802 lang=cpp
 *
 * [1802] Maximum Value at a Given Index in a Bounded Array
 */

// @lc code=start
#include <algorithm>
class Solution 
{
public:
    int maxValue(int n, int index, int maxSum) 
    {
        int left = 0;
        int right = maxSum + 1;
        
        while (left < right)
        {
            long k = left + (right - left) / 2;
            long S = k * k;
            long leftLim = (long)(index) - k + 1;
            long rightLim = (long)(n - index) - k;
            S += std::max(leftLim, (long) 0);
            S += std::max(rightLim, (long) 0);
            
            if (leftLim < (long) 0)
            {
                S -= (k - index - 1) * (k - index) / 2;
            }
            
            if (rightLim <= -1)
            {
                S -= (k - (n - index)) * (k - n + index + 1) / 2;
            }
            
            if (S <= (long) maxSum)
            {
                left = k + 1;
            }
            else
            {
                right = k;
            }
        }
        
        return left - 1;
    }
};
// @lc code=end

