/*
 * @lc app=leetcode id=205 lang=cpp
 *
 * [205] Isomorphic Strings
 */

// @lc code=start
#include <unordered_map>
#include <unordered_set>
#include <string>

class Solution {
public:
    bool isIsomorphic(std::string s, std::string t) {
        std::unordered_map<char, char> hashTable;
        std::unordered_set<char> seen;
        for (int i = 0; i < s.length(); i++) {
            if ((!hashTable.count(s[i]) && seen.count(t[i])) || (hashTable.count(s[i]) && t[i] != hashTable[s[i]])) {
                return false;
            }
            hashTable[s[i]] = t[i];
            seen.insert(t[i]);
        }
        return true;
    }
};

// @lc code=end

