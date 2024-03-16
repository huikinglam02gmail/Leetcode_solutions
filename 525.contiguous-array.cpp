/*
 * @lc app=leetcode id=525 lang=cpp
 *
 * [525] Contiguous Array
 */

// @lc code=start
#include <vector>
#include <unordered_map>
#include <algorithm>

class Solution {
public:
    int findMaxLength(std::vector<int>& nums) {
        std::unordered_map<int, std::vector<int>> hashTable;
        hashTable[0] = {-1, -1};
        int total = 0;
        int result = 0;
        for (int i = 0; i < nums.size(); i++) {
            if (nums[i] == 0) total--;
            else total++;
            
            if (hashTable.find(total) == hashTable.end()) {
                hashTable[total] = {i, i};
            } else {
                auto& indexes = hashTable[total];
                indexes[1] = i;
            }
        }
        
        for (auto& pair : hashTable) {
            result = std::max(result, pair.second[1] - pair.second[0]);
        }
        
        return result;
    }
};

// @lc code=end

