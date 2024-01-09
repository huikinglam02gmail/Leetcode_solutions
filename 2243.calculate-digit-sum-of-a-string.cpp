/*
 * @lc app=leetcode id=2243 lang=cpp
 *
 * [2243] Calculate Digit Sum of a String
 */

// @lc code=start
#include <iostream>
#include <queue>
#include <vector>
#include <string>

class Solution {
public:
    /**
    Just simulate with a queue
    */
    std::string digitSum(std::string s, int k) {
        std::queue<int> dq;
        for (char c : s) {
            dq.push(c - '0');
        }

        while (dq.size() > k) {
            int count = 0;
            std::vector<int> current = {0};

            while (!dq.empty()) {
                while (count < k && !dq.empty()) {
                    count++;
                    current.back() += dq.front();
                    dq.pop();
                }

                if (!dq.empty()) {
                    count = 0;
                    current.push_back(0);
                }
            }

            for (int num : current) {
                std::string numString = std::to_string(num);
                for (char c : numString) {
                    dq.push(c - '0');
                }
            }
        }

        std::string result = "";
        while (!dq.empty()) {
            result += std::to_string(dq.front());
            dq.pop();
        }

        return result;
    }
};

// @lc code=end

