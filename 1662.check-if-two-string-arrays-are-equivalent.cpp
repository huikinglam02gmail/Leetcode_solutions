/*
 * @lc app=leetcode id=1662 lang=cpp
 *
 * [1662] Check If Two String Arrays are Equivalent
 */

// @lc code=start
#include <vector>
#include <string>

class Solution {
public:
    bool arrayStringsAreEqual(std::vector<std::string>& word1, std::vector<std::string>& word2) {
        return concatenateStrings(word1) == concatenateStrings(word2);
    }

private:
    std::string concatenateStrings(const std::vector<std::string>& words) {
        std::string result;
        for (const std::string& word : words) {
            result += word;
        }
        return result;
    }
};

// @lc code=end

