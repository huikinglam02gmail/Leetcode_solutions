/*
 * @lc app=leetcode id=557 lang=cpp
 *
 * [557] Reverse Words in a String III
 */

// @lc code=start
#include <vector>
#include <sstream>

class Solution {
public:
    std::string reverseWords(std::string s) {
        std::vector<std::string> words;
        std::istringstream iss(s);
        std::string word;

        while (iss >> word) {
            std::reverse(word.begin(), word.end());
            words.push_back(word);
        }

        std::string result;
        for (const std::string& w : words) {
            if (!result.empty()) {
                result += " ";
            }
            result += w;
        }

        return result;
    }
};

// @lc code=end

