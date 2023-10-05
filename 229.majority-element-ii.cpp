/*
 * @lc app=leetcode id=229 lang=cpp
 *
 * [229] Majority Element II
 */

// @lc code=start
#include <vector>
#include <unordered_map>

class Solution {
public:
    std::vector<int> majorityElement(std::vector<int>& nums) {
        std::unordered_map<int, int> hashTable;
        int n = nums.size();
        
        for (int num : nums) {
            hashTable[num]++;
        }
        
        std::vector<int> result;
        
        for (const auto& entry : hashTable) {
            if (entry.second > n / 3) {
                result.push_back(entry.first);
            }
        }
        
        return result;
    }
};

// @lc code=end

