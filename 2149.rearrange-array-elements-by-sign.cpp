/*
 * @lc app=leetcode id=2149 lang=cpp
 *
 * [2149] Rearrange Array Elements by Sign
 */

// @lc code=start
#include <vector>
using namespace std;

class Solution {
public:
    vector<int> rearrangeArray(vector<int>& nums) {
        vector<vector<int>> arrs(2, vector<int>());
        
        bool firstIsPositive = nums[0] > 0;
        
        for (int num : nums) {
            arrs[(num > 0) ^ firstIsPositive ? 1 : 0].push_back(num);
        }
        
        vector<int> result;
        
        for (int i = 0; i < nums.size() / 2; i++) {
            result.push_back(arrs[1 - (firstIsPositive ? 1 : 0)][i]);
            result.push_back(arrs[firstIsPositive ? 1 : 0][i]);
        }
        
        return result;
    }
};

// @lc code=end

