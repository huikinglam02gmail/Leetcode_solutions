/*
 * @lc app=leetcode id=645 lang=cpp
 *
 * [645] Set Mismatch
 */

// @lc code=start
#include <vector>
#include <unordered_set>

class Solution {
public:
    std::vector<int> findErrorNums(std::vector<int>& nums) {
        std::unordered_set<int> hashSet;
        int n = nums.size();
        std::vector<int> result;
        int total = 0;

        for (int num : nums) {
            if (hashSet.find(num) == hashSet.end()) {
                hashSet.insert(num);
                total += num;
            } else {
                result.push_back(num);
            }
        }

        result.push_back(n * (n + 1) / 2 - total);
        return result;
    }
};

// @lc code=end

