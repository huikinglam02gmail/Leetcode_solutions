/*
 * @lc app=leetcode id=1849 lang=cpp
 *
 * [1849] Splitting a String Into Descending Consecutive Values
 */

// @lc code=start
#include <string>
#include <cmath>

class Solution {
private:
    std::string s;

public:
    bool Backtracking(int start, int end, long long inFront) {
        if (inFront > 0) {
            long long total;
            try {
                total = std::stoll(s.substr(start, end - start + 1));
            } catch (std::out_of_range&) {
                total = -1;
            }
            
            if (total == inFront - 1) {
                return true;
            }
        }

        int i = start + 1;
        while (i < end + 1) {
            long long front;
            try {
                front = std::stoll(s.substr(start, i - start));
            } catch (std::out_of_range&) {
                break;
            }
            
            if (std::to_string(front).length() > end + 2 - i) {
                break;
            } else if ((inFront < 0 || inFront - 1 == front) && Backtracking(i, end, front)) {
                return true;
            } else {
                ++i;
            }
        }
        return false;
    }

    bool splitString(std::string s) {
        this->s = s;
        int n = s.length();
        return Backtracking(0, n - 1, -1);
    }
};
// @lc code=end

