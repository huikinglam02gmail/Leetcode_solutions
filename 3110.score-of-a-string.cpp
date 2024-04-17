/*
 * @lc app=leetcode id=3110 lang=cpp
 *
 * [3110] Score of a String
 */

// @lc code=start
#include <string>
#include <cmath>

using namespace std;

class Solution {
public:
    int scoreOfString(string s) {
        int n = s.size();
        int result = 0;
        for (int i = 0; i < n - 1; i++) {
            result += abs(s[i + 1] - s[i]);
        }
        return result;
    }
};

// @lc code=end

