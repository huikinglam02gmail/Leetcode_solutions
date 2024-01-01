/*
 * @lc app=leetcode id=455 lang=cpp
 *
 * [455] Assign Cookies
 */

// @lc code=start
#include <vector>
#include <algorithm>

class Solution {
public:
    int findContentChildren(std::vector<int>& g, std::vector<int>& s) {
        std::sort(g.begin(), g.end());
        std::sort(s.begin(), s.end());

        int content = 0;
        int ps = 0;

        while (content < g.size() && ps < s.size()) {
            if (s[ps] >= g[content]) {
                content++;
            }
            ps++;
        }

        return content;
    }
};

// @lc code=end

