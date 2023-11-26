/*
 * @lc app=leetcode id=2947 lang=cpp
 *
 * [2947] Count Beautiful Substrings I
 */

// @lc code=start
#include <string>
#include <unordered_set>

class Solution {
public:
    int beautifulSubstrings(std::string s, int k) {
        int N = s.size();
        std::unordered_set<char> vowels {'a', 'e', 'i', 'o', 'u'};
        int ans = 0;

        for (int i = 0; i < N; i++) {
            int c = 0, v = 0;

            for (int j = i; j < N; j++) {
                if (vowels.count(s[j])) {
                    v++;
                } else {
                    c++;
                }

                ans += (c == v && (v * c % k == 0));
            }
        }

        return ans;
    }
};

// @lc code=end

