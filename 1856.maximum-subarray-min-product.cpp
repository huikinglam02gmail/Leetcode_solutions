/*
 * @lc app=leetcode id=1856 lang=cpp
 *
 * [1856] Maximum Subarray Min-Product
 */

// @lc code=start
#include <vector>
#include <algorithm>
#include <stack>
using std::max;

class Solution {
public:
    int maxSumMinProduct(std::vector<int>& nums) {
        std::vector<long long> prefix(1, 0);
        for (int num : nums) {
            prefix.push_back(prefix.back() + (long long)num);
        }
        
        std::stack<int> stack;
        stack.push(-1);
        std::vector<int> Nums = nums;
        Nums.push_back(-1);
        long long result = 0;
        long long MOD = 1000000007;
        for (int i = 0; i < Nums.size(); i++) {
            while (!stack.empty() && Nums[(stack.top() + Nums.size()) % Nums.size()] > Nums[i]) {
                int j = stack.top();
                stack.pop();
                result = max(result, (long long)Nums[j] * (prefix[i] - prefix[stack.top() + 1]));
            }
            stack.push(i);
        }
        return static_cast<int>(result % MOD);
    }
};
// @lc code=end

