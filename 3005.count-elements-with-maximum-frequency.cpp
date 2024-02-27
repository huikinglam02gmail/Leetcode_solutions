/*
 * @lc app=leetcode id=3005 lang=cpp
 *
 * [3005] Count Elements With Maximum Frequency
 */

// @lc code=start
#include <vector>
#include <unordered_map>

class Solution {
public:
    int maxFrequencyElements(std::vector<int>& nums) {
        std::unordered_map<int, int> hashTable;
        for (int num : nums) {
            hashTable[num]++;
        }
        
        int maxOccur = 0;
        int result = 0;
        for (auto& entry : hashTable) {
            if (entry.second > maxOccur) {
                maxOccur = entry.second;
                result = 0;
            }
            if (entry.second == maxOccur) {
                result += entry.second;
            }
        }
        
        return result;
    }
};

// @lc code=end

