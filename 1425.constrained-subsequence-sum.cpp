/*
 * @lc app=leetcode id=1425 lang=cpp
 *
 * [1425] Constrained Subsequence Sum
 */

// @lc code=start
#include <vector>
#include <queue>

using std::max;

class Solution {
public:
    int constrainedSubsetSum(std::vector<int>& nums, int k) {
        int result = INT_MIN;
        std::priority_queue<std::pair<int, int>> maxHeap;
        int n = nums.size();
        
        for (int i = 0; i < n; ++i) {
            while (!maxHeap.empty() && i - maxHeap.top().second > k) {
                maxHeap.pop();
            }
            
            int maxSoFar = 0;
            if (!maxHeap.empty()) {
                maxSoFar = max(maxSoFar, maxHeap.top().first);
            }
            
            result = max(result, nums[i] + maxSoFar);
            maxHeap.push(std::make_pair(nums[i] + maxSoFar, i));
        }
        
        return result;
    }
};

// @lc code=end

