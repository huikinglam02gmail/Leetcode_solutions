/*
 * @lc app=leetcode id=2956 lang=cpp
 *
 * [2956] Find Common Elements Between Two Arrays
 */

// @lc code=start
#include <vector>
#include <unordered_map>

class Solution {
public:
    std::vector<int> findIntersectionValues(std::vector<int>& nums1, std::vector<int>& nums2) {
        std::unordered_map<int, int> hashTable1, hashTable2;
        
        for (int num : nums1) {
            hashTable1[num]++;
        }
        
        for (int num : nums2) {
            hashTable2[num]++;
        }
        
        std::vector<int> result(2);
        
        for (auto& entry : hashTable1) {
            if (hashTable2.count(entry.first)) {
                result[0] += entry.second;
            }
        }
        
        for (auto& entry : hashTable2) {
            if (hashTable1.count(entry.first)) {
                result[1] += entry.second;
            }
        }
        
        return result;
    }
};

// @lc code=end

