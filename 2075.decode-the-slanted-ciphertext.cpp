/*
 * @lc app=leetcode id=2075 lang=cpp
 *
 * [2075] Decode the Slanted Ciphertext
 */

// @lc code=start
#include <string>
#include <vector>

class Solution {
public:
    std::string decodeCiphertext(std::string encodedText, int rows) {
        std::string result;
        int cols = encodedText.length() / rows;
        for (int i = 0; i < cols; i++) {
            int cur = i;
            while (cur < encodedText.length()) {
                result += encodedText[cur];
                cur += cols + 1;
            }
        }
        while (!result.empty() && result[result.length() - 1] == ' ') {
            result.pop_back();
        }
        return result;
    }
};

// @lc code=end

