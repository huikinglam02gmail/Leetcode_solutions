/*
 * @lc app=leetcode id=2224 lang=cpp
 *
 * [2224] Minimum Number of Operations to Convert Time
 */

// @lc code=start
#include <string>

class Solution {
public:
    int convertTime(std::string current, std::string correct) {
        int correctTime = stoi(correct.substr(0, 2)) * 60 + stoi(correct.substr(3));
        int currentTime = stoi(current.substr(0, 2)) * 60 + stoi(current.substr(3));
        int result = 0;

        for (int increment : {60, 15, 5, 1}) {
            int inc = (correctTime - currentTime) / increment;
            currentTime += inc * increment;
            result += inc;
        }

        return result;
    }
};

// @lc code=end

