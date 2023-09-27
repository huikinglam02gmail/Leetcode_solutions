/*
 * @lc app=leetcode id=880 lang=cpp
 *
 * [880] Decoded String at Index
 */

// @lc code=start
#include <string>

class Solution {
public:
    std::string decodeAtIndex(std::string s, int k) {
        long long size = 0;
        long long kLong = static_cast<long long>(k);
        
        for (char c : s) {
            if (std::isalpha(c)) {
                size++;
            }
            else {
                size *= static_cast<long long>(c - '0');
            }
        }
        
        for (auto it = s.rbegin(); it != s.rend(); ++it) {
            kLong %= size;
            
            if (kLong == 0 && std::isalpha(*it)) {
                return std::string(1, *it);
            }
            
            if (std::isalpha(*it)) {
                size--;
            }
            else {
                size /= static_cast<long long>(*it - '0');
            }
        }
        
        return ""; // Return empty string if no result is found.
    }
};

// @lc code=end

