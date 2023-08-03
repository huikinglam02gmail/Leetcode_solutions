/*
 * @lc app=leetcode id=17 lang=cpp
 *
 * [17] Letter Combinations of a Phone Number
 */

// @lc code=start
#include <iostream>
#include <vector>
#include <unordered_map>

class Solution {
private:
    std::unordered_map<char, std::string> hashTable = {
        {'2', "abc"}, {'3', "def"}, {'4', "ghi"}, {'5', "jkl"},
        {'6', "mno"}, {'7', "pqrs"}, {'8', "tuv"}, {'9', "wxyz"}
    };

    std::vector<std::string> result;
    std::string digits;

    void DFS(int pos, std::string currentString) {
        if (pos == digits.length()) {
            if (!currentString.empty()) {
                result.push_back(currentString);
            }
        }
        else {
            std::string s = hashTable[digits[pos]];
            for (char c : s) {
                DFS(pos + 1, currentString + c);
            }
        }
    }

public:
    std::vector<std::string> letterCombinations(std::string digits) {
        result.clear();
        this->digits = digits;
        DFS(0, "");
        return result;
    }
};

// @lc code=end

