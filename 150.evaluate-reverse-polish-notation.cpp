/*
 * @lc app=leetcode id=150 lang=cpp
 *
 * [150] Evaluate Reverse Polish Notation
 */

// @lc code=start
#include <vector>
#include <stack>
#include <string>

class Solution {
public:
    int evalRPN(std::vector<std::string>& tokens) {
        if (tokens.size() == 1) {
            return std::stoi(tokens[0]);
        } else {
            std::stack<int> stack;
            for (const std::string& token : tokens) {
                if (token != "+" && token != "-" && token != "*" && token != "/") {
                    stack.push(std::stoi(token));
                } else {
                    int right = stack.top();
                    stack.pop();
                    int left = stack.top();
                    stack.pop();
                    if (token == "+") {
                        stack.push(left + right);
                    } else if (token == "-") {
                        stack.push(left - right);
                    } else if (token == "*") {
                        stack.push(left * right);
                    } else {
                        stack.push(left / right);
                    }
                }
            }
            return stack.top();
        }
    }
};

// @lc code=end

