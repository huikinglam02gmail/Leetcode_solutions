/*
 * @lc app=leetcode id=2899 lang=cpp
 *
 * [2899] Last Visited Integers
 */

// @lc code=start
#include <vector>

class Solution {
public:
    std::vector<int> lastVisitedIntegers(std::vector<int>& nums) {
        int k = 0;
        std::vector<int> seen;
        std::vector<int> ans;
        for (int num : nums) {
            if (num > 0) {
                seen.push_back(num);
                k = 0;
            } else {
                k++;
                int n = seen.size();
                if (k <= n) {
                    ans.push_back(seen[n - k]);
                } else {
                    ans.push_back(num);
                }
            }
        }
        return ans;
    }
};

// @lc code=end

