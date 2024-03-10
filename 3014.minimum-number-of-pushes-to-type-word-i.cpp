/*
 * @lc app=leetcode id=3014 lang=cpp
 *
 * [3014] Minimum Number of Pushes to Type Word I
 */

// @lc code=start
#include <string>

using namespace std;

class Solution {
public:
    int minimumPushes(string word) {
        int result = 0;
        int n = word.size();
        for (int i = 0; i < n; i++) {
            result += 1 + (i / 8);
        }
        return result;
    }
};

// @lc code=end

