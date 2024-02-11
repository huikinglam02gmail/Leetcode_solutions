/*
 * @lc app=leetcode id=2815 lang=cpp
 *
 * [2815] Max Pair Sum in an Array
 */

// @lc code=start
#include <vector>
#include <string>
#include <algorithm>

class Solution {
public:
    int maxSum(std::vector<int>& nums) {
        std::vector<std::vector<int>> hashTable(10);
        
        for (int num : nums) {
            std::string numString = std::to_string(num);
            int maxDigit = 0;
            for (char c : numString) {
                maxDigit = std::max(maxDigit, c - '0');
            }
            hashTable[maxDigit].push_back(num);
        }
        
        int result = -1;
        for (int i = 0; i < 10; i++) {
            if (hashTable[i].size() >= 2) {
                std::sort(hashTable[i].begin(), hashTable[i].end());
                result = std::max(result, hashTable[i].back() + hashTable[i][hashTable[i].size() - 2]);
            }
        }
        
        return result;
    }
};

// @lc code=end

