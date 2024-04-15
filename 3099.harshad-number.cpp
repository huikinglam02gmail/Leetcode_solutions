/*
 * @lc app=leetcode id=3099 lang=cpp
 *
 * [3099] Harshad Number
 */

// @lc code=start
#include <string>
using namespace std;

class Solution {
public:
    int sumOfTheDigitsOfHarshadNumber(int x) {
        int S = 0;
        string strX = to_string(x);
        for (char c : strX) {
            S += c - '0';
        }
        return (x % S == 0) ? S : -1;
    }
};

// @lc code=end

