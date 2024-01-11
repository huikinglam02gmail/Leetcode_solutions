/*
 * @lc app=leetcode id=2437 lang=cpp
 *
 * [2437] Number of Valid Clock Times
 */

// @lc code=start
#include <iostream>
#include <vector>
#include <string>

class Solution {
public:
    /*
    Just try whatever combinations
    */
    bool validTime(const std::string& time) {
        if (std::stoi(time.substr(0, 2)) > 23 || std::stoi(time.substr(3)) > 59) {
            return false;
        }
        return 0 <= std::stoi(time.substr(0, 2)) * 60 + std::stoi(time.substr(3)) && std::stoi(time.substr(0, 2)) * 60 + std::stoi(time.substr(3)) <= 23 * 60 + 59;
    }
    
    int countTime(const std::string& time) {
        std::vector<std::string> pos;
        pos.push_back("");
        for (char c : time) {
            std::vector<std::string> newPos;
            if (c != '?') {
                for (const std::string& p : pos) {
                    newPos.push_back(p + c);
                }
            } else {
                for (const std::string& p : pos) {
                    for (int i = 0; i < 10; i++) {
                        newPos.push_back(p + std::to_string(i));
                    }
                }
            }
            pos = newPos;
        }
        int result = 0;
        for (const std::string& p : pos) {
            if (validTime(p)) {
                result++;
            }
        }
        return result;
    }
};

// @lc code=end

