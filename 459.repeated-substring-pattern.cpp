/*
 * @lc app=leetcode id=459 lang=cpp
 *
 * [459] Repeated Substring Pattern
 */

// @lc code=start
#include <string>
using std::string;

class Solution {
private:
    string repeat(string s, int n) {
        string s1 = s;
        for (int i=1; i<n;i++)
            s += s1; // Concatinating strings
        return s;
    }
public:
    bool repeatedSubstringPattern(string s) {
        for (int i = 1; i <= s.length() / 2; i++) {
            if (s.length() % i == 0 && s == repeat(string(s.begin(), s.begin() + i), s.length() / i)) {
                return true;
            }
        }
        return false;
    }
};

// @lc code=end

