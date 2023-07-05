/*
 * @lc app=leetcode id=1493 lang=cpp
 *
 * [1493] Longest Subarray of 1's After Deleting One Element
 */

// @lc code=start
#include<vector>
#include<algorithm>
using std::max;
using std::vector;
class Solution {
public:
    int longestSubarray(vector<int>& nums) {
        int left = 0;
        int result = 0;
        int numZeros = 0;
        int n = nums.size();

        for (int right = 0; right < n; right++)
        {
            if (nums[right] == 0)
            {
                numZeros++;
            }
            while (numZeros > 1)
            {
                if (nums[left] == 0)
                {
                    numZeros--;
                }
                left++;
            }
            result = max(result, right - left);
        }
        return result;        
    }
};
// @lc code=end

