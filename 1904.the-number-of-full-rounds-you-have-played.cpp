/*
 * @lc app=leetcode id=1904 lang=cpp
 *
 * [1904] The Number of Full Rounds You Have Played
 */

// @lc code=start
#include <string>
#include <cmath>

class Solution {
public:
    /*
     * Convert the times to mins
     * if logout < login, + 24 * 60 to it
     * Then // 15
     */
    int CeilDiv(int a, int b) {
        return (a + b - 1) / b;
    }

    int numberOfRounds(std::string loginTime, std::string logoutTime) {
        int login = std::stoi(loginTime.substr(0, 2)) * 60 + std::stoi(loginTime.substr(3));
        int logout = std::stoi(logoutTime.substr(0, 2)) * 60 + std::stoi(logoutTime.substr(3));

        if (login > logout) {
            logout += 24 * 60;
        }

        return std::max(0, logout / 15 - CeilDiv(login, 15));
    }
};
// @lc code=end

