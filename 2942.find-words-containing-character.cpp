/*
 * @lc app=leetcode id=2942 lang=cpp
 *
 * [2942] Find Words Containing Character
 */

// @lc code=start
#include <vector>
#include <string>

class Solution {
public:
    std::vector<int> findWordsContaining(std::vector<std::string>& words, char x) {
        std::vector<int> result;
        for (int i = 0; i < words.size(); ++i) {
            if (words[i].find(x) != std::string::npos) {
                result.push_back(i);
            }
        }
        return result;
    }
};

// @lc code=end

