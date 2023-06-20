/*
 * @lc app=leetcode id=2090 lang=cpp
 *
 * [2090] K Radius Subarray Averages
 */

// @lc code=start
#include<vector>
#include<numeric>
using std::accumulate;
using std::vector;
class Solution {
public:
    vector<int> getAverages(vector<int>& nums, int k) {
        int n = nums.size();
        vector<int> result;
        result.resize(n, -1);
        if (n >= 2 * k + 1)
        {
            long long windowSum = accumulate(nums.begin(), nums.begin() + 2 * k + 1, (long long)0);
            int i = k;
            while (i <= n - k - 1)
            {
                result[i] = (int)(windowSum / (long long)(2 * k + 1));
                windowSum -= (long long)(nums[i - k]);
                if (i + k + 1 < n)
                {
                    windowSum += (long long)(nums[i + k + 1]);
                }
                i++;
            }
        }
        return result;        
    }
};
// @lc code=end

