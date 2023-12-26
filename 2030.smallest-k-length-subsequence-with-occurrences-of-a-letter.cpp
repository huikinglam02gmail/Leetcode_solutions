/*
 * @lc app=leetcode id=2030 lang=cpp
 *
 * [2030] Smallest K-Length Subsequence With Occurrences of a Letter
 */

// @lc code=start
#include <string>
#include <vector>

class Solution {
public:
    std::string smallestSubsequence(std::string s, int k, char letter, int repetition) {
        std::string stack;
        int n = s.length();
        int usableLetterBehind = std::count(s.begin(), s.end(), letter);

        for (int i = 0; i < n; i++) {
            char c = s[i];
            while (!stack.empty() && c < stack.back() && n - i + stack.size() > k && (stack.back() != letter || usableLetterBehind > repetition)) {
                if (stack.back() == letter) repetition += 1;
                stack.pop_back();
            }

            if (c == letter) usableLetterBehind -= 1;

            if (stack.size() < k) {
                if (c == letter) {
                    stack += c;
                    repetition -= 1;
                } else if (k - (int)stack.size() > repetition) {
                    stack += c;
                }
            }
        }

        return stack;
    }
};

// @lc code=end

