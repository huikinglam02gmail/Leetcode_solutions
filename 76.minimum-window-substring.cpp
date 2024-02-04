/*
 * @lc app=leetcode id=76 lang=cpp
 *
 * [76] Minimum Window Substring
 */

// @lc code=start
#include <string>
#include <unordered_map>

class Solution {
public:
    std::string minWindow(std::string s, std::string t) {
        std::unordered_map<char, int> need;
        int missing = t.length(), i = 0, I = -1, J = -1;

        for (char c : t) {
            if (need.find(c) != need.end()) {
                need[c]++;
            } else {
                need[c] = 1;
            }
        }

        for (int j = 0; j < s.length(); j++) {
            char c = s[j];
            if (need.find(c) == need.end()) need[c] = 0;
            if (need[c] > 0) {
                missing--;
            }
            need[c]--;

            if (missing == 0) {
                while (i < j && (need.find(s[i]) != need.end() && need[s[i]] < 0)) {
                    need[s[i]]++;
                    i++;
                }

                if (J == -1 || j - i <= J - I) {
                    I = i;
                    J = j;
                }
            }
        }

        if (missing == 0) {
            return s.substr(I, J - I + 1);
        } else {
            return "";
        }
    }
};

// @lc code=end

