/*
 * @lc app=leetcode id=1160 lang=cpp
 *
 * [1160] Find Words That Can Be Formed by Characters
 */

// @lc code=start
#include <vector>

class Solution {
public:
    int countCharacters(std::vector<std::string>& words, std::string& chars) {
        std::vector<int> hashChars(26, 0);
        for (char c : chars) {
            hashChars[c - 'a']++;
        }

        int result = 0;
        for (const std::string& word : words) {
            std::vector<int> hashWord(26, 0);
            for (char c : word) {
                hashWord[c - 'a']++;
            }

            if (isWordFormed(hashWord, hashChars)) {
                result += word.length();
            }
        }

        return result;
    }

private:
    bool isWordFormed(const std::vector<int>& hashWord, const std::vector<int>& hashChars) {
        for (int i = 0; i < 26; i++) {
            if (hashWord[i] > hashChars[i]) {
                return false;
            }
        }
        return true;
    }
};

// @lc code=end

