/*
 * @lc app=leetcode id=1829 lang=cpp
 *
 * [1829] Maximum XOR for Each Query
 */

// @lc code=start
#include <vector>
using namespace std;

class Solution {
public:
    vector<int> getMaximumXor(vector<int>& nums, int maximumBit) {
        int XOR = 0;
        for (int num : nums) {
            XOR ^= num;
        }
        int n = nums.size();
        vector<int> result;
        for (int i = 0; i < n; i++) {
            result.push_back(((1 << maximumBit) - 1) ^ XOR);
            XOR ^= nums[n - i - 1];
        }
        return result;
    }
};

// @lc code=end

