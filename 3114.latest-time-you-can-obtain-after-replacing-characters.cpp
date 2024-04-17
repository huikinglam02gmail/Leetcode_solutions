/*
 * @lc app=leetcode id=3114 lang=cpp
 *
 * [3114] Latest Time You Can Obtain After Replacing Characters
 */

// @lc code=start
#include <string>
#include <vector>

using namespace std;

class Solution {
private:
    vector<string> result;

public:
    Solution() {
        result.reserve(720); // Reserve space for 720 elements
        for (int i = 719; i >= 0; --i) {
            result.push_back(to_string(i / 60 / 10) + to_string(i / 60 % 10) + ":" +
                             to_string(i % 60 / 10) + to_string(i % 60 % 10));
        }
    }

    string findLatestTime(string s) {
        for (const string& t : result) {
            if ((s[0] == '?' || s[0] == t[0]) &&
                (s[1] == '?' || s[1] == t[1]) &&
                (s[3] == '?' || s[3] == t[3]) &&
                (s[4] == '?' || s[4] == t[4])) {
                return t;
            }
        }
        return "";
    }
};

// @lc code=end

