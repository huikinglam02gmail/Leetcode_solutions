/*
 * @lc app=leetcode id=1704 lang=cpp
 *
 * [1704] Determine if String Halves Are Alike
 */

// @lc code=start
#include <unordered_set>

class Solution {
public:
    bool halvesAreAlike(std::string s) {
        std::unordered_set<char> vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'};
        int left = 0;
        int right = 0;
        for (int i = 0; i < s.length(); i++) {
            if (vowels.count(s[i])) {
                if (i < s.length() / 2) {
                    left += 1;
                } else {
                    right += 1;
                }
            }
        }
        return left == right;
    }
};

// @lc code=end

