/*
 * @lc app=leetcode id=1793 lang=cpp
 *
 * [1793] Maximum Score of a Good Subarray
 */

// @lc code=start
#include<vector>
#include<algorithm>
using std::max;
using std::min;
using std::vector;
class Solution {
public:
    int maximumScore(vector<int>& nums, int k) {
        int result = nums[k];
        int minSoFar = nums[k];
        int i = k;
        int j = k;
        int n = nums.size();

        while (i >= 0 && j <= n - 1)
        {
            minSoFar = min(minSoFar, nums[i]);
            minSoFar = min(minSoFar, nums[j]);
            result = max(result, minSoFar * (j - i + 1));

            if (i == 0)
            {
                j++;
            }
            else if (j == n - 1)
            {
                i--;
            }
            else if (nums[i - 1] < nums[j + 1])
            {
                j++;
            }
            else
            {
                i--;
            }
        }

        return result;        
    }
};
// @lc code=end

