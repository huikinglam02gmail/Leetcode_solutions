/*
 * @lc app=leetcode id=402 lang=cpp
 *
 * [402] Remove K Digits
 */

// @lc code=start
#include <string>
#include <stack>
#include <algorithm>

class Solution {
public:
    std::string removeKdigits(std::string num, int k) {
        std::stack<char> stack;

        for (char c : num) {
            while (!stack.empty() && stack.top() > c && k > 0) {
                stack.pop();
                k--;
            }
            stack.push(c);
        }

        while (k > 0) {
            stack.pop();
            k--;
        }

        if (stack.empty()) {
            return "0";
        } else {
            std::string result;
            while (!stack.empty()) {
                result += stack.top();
                stack.pop();
            }
            std::reverse(result.begin(), result.end());
            int i = 0;
            while (i < result.length() && result[i] == '0') {
                i++;
            }
            if (i == result.length()) {
                return "0";
            } else {
                return result.substr(i);
            }
        }
    }
};

// @lc code=end

