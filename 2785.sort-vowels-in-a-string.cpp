/*
 * @lc app=leetcode id=2785 lang=cpp
 *
 * [2785] Sort Vowels in a String
 */

// @lc code=start
#include <string>
#include <vector>
#include <algorithm>

class Solution {
public:
    std::string sortVowels(std::string s) {
        std::vector<char> vowels;
        std::vector<int> indices;
        std::vector<char> result(s.begin(), s.end());

        for (int i = 0; i < s.length(); i++) {
            char c = s[i];
            if (isVowel(c)) {
                vowels.push_back(c);
                indices.push_back(i);
            }
        }

        std::sort(vowels.begin(), vowels.end());

        for (int i = 0; i < vowels.size(); i++) {
            result[indices[i]] = vowels[i];
        }

        return std::string(result.begin(), result.end());
    }

private:
    bool isVowel(char c) {
        return (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u' ||
                c == 'A' || c == 'E' || c == 'I' || c == 'O' || c == 'U');
    }
};

// @lc code=end

