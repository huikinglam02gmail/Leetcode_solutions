/*
 * @lc app=leetcode id=3019 lang=cpp
 *
 * [3019] Number of Changing Keys
 */

// @lc code=start
#include <string>

using namespace std;

class Solution {
public:
    int countKeyChanges(string s) {
        int result = 0;
        int n = s.size();
        for (int i = 0; i < n - 1; i++) {
            if (tolower(s[i + 1]) != tolower(s[i])) result++;
        }
        return result;
    }
};

// @lc code=end

