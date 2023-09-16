/*
 * @lc app=leetcode id=1898 lang=cpp
 *
 * [1898] Maximum Number of Removable Characters
 */

// @lc code=start
#include <string>
#include <vector>
#include <unordered_map>

class Solution {
private:
    std::unordered_map<int, int> reverseRemovable;
public:
    bool isSubsequence(std::string s, std::string t, int mid) {
        int p1 = 0, p2 = 0;
        while (p1 < s.length() && p2 < t.length()) {
            if (s[p1] == t[p2] && (reverseRemovable.find(p2) == reverseRemovable.end() || reverseRemovable[p2] >= mid)) {
                p1++;
            }
            p2++;
        }
        return p1 == s.length();
    }

    int maximumRemovals(std::string s, std::string p, std::vector<int>& removable) {
        int l = 0, r = removable.size();
        reverseRemovable.clear();
        for (int i = 0; i < removable.size(); i++) {
            reverseRemovable[removable[i]] = i;
        }
        while (l < r) {
            int mid = l + (r - l) / 2;
            if (isSubsequence(p, s, mid)) {
                l = mid + 1;
            } else {
                r = mid;
            }
        }
        if (l == removable.size() && isSubsequence(p, s, l)) {
            return l;
        } else {
            return l - 1;
        }
    }
};

// @lc code=end

