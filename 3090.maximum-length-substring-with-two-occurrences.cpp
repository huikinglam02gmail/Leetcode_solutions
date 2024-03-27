/*
 * @lc app=leetcode id=3090 lang=cpp
 *
 * [3090] Maximum Length Substring With Two Occurrences
 */

// @lc code=start
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    int maximumLengthSubstring(string s) {
        int left = 0;
        vector<int> seen(26, 0);
        int result = 0;
        for (int right = 0; right < s.length(); right++) {
            char c = s[right];
            while (seen[c - 'a'] == 2) {
                seen[s[left] - 'a'] -= 1;
                left += 1;
            }
            seen[c - 'a'] += 1;
            result = max(result, right - left + 1);
        }
        return result;
    }
};

// @lc code=end

