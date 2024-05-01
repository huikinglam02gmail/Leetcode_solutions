/*
 * @lc app=leetcode id=2000 lang=cpp
 *
 * [2000] Reverse Prefix of Word
 */

// @lc code=start
#include <string>
using namespace std;

class Solution {
public:
    string reversePrefix(string word, char ch) {
        int i = 0;
        int n = word.length();
        while (i < n && word[i] != ch) {
            i++;
        }
        if (i == n) {
            return word;
        }
        reverse(word.begin(), word.begin() + i + 1);
        return word;
    }
};

// @lc code=end

