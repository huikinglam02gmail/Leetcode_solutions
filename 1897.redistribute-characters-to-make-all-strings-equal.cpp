/*
 * @lc app=leetcode id=1897 lang=cpp
 *
 * [1897] Redistribute Characters to Make All Strings Equal
 */

// @lc code=start
#include <vector>
#include <string>

class Solution {
public:
    bool makeEqual(std::vector<std::string>& words) {
        std::vector<int> hashTable(26, 0);
        
        for (const std::string& word : words) {
            for (char c : word) {
                hashTable[c - 'a']++;
            }
        }
        
        for (int count : hashTable) {
            if (count % words.size() != 0) {
                return false;
            }
        }
        
        return true;
    }
};

// @lc code=end

