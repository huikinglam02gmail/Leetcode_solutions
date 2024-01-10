/*
 * @lc app=leetcode id=2255 lang=cpp
 *
 * [2255] Count Prefixes of a Given String
 */

// @lc code=start
#include <vector>
#include <string>

class Solution {
public:
    int countPrefixes(std::vector<std::string>& words, std::string& s) {
        int result = 0;
        for (const std::string& word : words) {
            if (s.compare(0, word.length(), word) == 0) {
                result++;
            }
        }
        return result;
    }
};

// @lc code=end

