/*
 * @lc app=leetcode id=58 lang=cpp
 *
 * [58] Length of Last Word
 */

// @lc code=start
#include <string>

class Solution {
public:
    /**
     * Add " " in front and after s
     * Pick up where s[i] == " " and s[i + 1] != " ", and s[j] != " " and s[j + 1] == " "
     */
    int lengthOfLastWord(std::string s) {
        s = " " + s + " ";
        int l = 0, r = 0;
        for (int i = 0; i < s.length() - 1; i++) {
            if (s[i] == ' ' && s[i + 1] != ' ') {
                l = i;
            }
            if (s[i] != ' ' && s[i + 1] == ' ') {
                r = i;
            }
        }
        return r - l;
    }
};

// @lc code=end

