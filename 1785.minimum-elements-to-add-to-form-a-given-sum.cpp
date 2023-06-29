/*
 * @lc app=leetcode id=1785 lang=cpp
 *
 * [1785] Minimum Elements to Add to Form a Given Sum
 */

// @lc code=start
#include <vector>
#include <algorithm>
#include <numeric>
using std::abs;
using std::accumulate;
using std::vector;
class Solution {
public:
    int minElements(vector<int>& nums, int limit, int goal) {
        vector<long long> Nums(nums.begin(), nums.end());
        return (int)((abs(accumulate(Nums.begin(), Nums.end(), (long long)0) - (long long)goal) + (long long)limit - (long long)1) / (long long)limit);        
    }
};
// @lc code=end

