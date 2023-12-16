/*
 * @lc app=leetcode id=242 lang=cpp
 *
 * [242] Valid Anagram
 */

// @lc code=start
#include <vector>

class Solution {
public:
    bool isAnagram(std::string s, std::string t) {
        if (s.length() != t.length()) return false;

        std::vector<int> sCount(26, 0);
        std::vector<int> tCount(26, 0);

        for (int i = 0; i < s.length(); i++) {
            sCount[s[i] - 'a']++;
            tCount[t[i] - 'a']++;
        }

        for (int i = 0; i < 26; i++) {
            if (sCount[i] != tCount[i]) return false;
        }

        return true;
    }
};

// @lc code=end

