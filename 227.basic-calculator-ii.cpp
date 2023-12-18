/*
 * @lc app=leetcode id=227 lang=cpp
 *
 * [227] Basic Calculator II
 */

// @lc code=start
#include <iostream>
#include <stack>
#include <unordered_map>

using namespace std;

class Solution {
public:
    int calculation(int current) {
        char oldOp = opStack.top();
        opStack.pop();
        int oldCurrent = numStack.top();
        numStack.pop();
        if (oldOp == '+') {
            current += oldCurrent;
        } else if (oldOp == '-') {
            current = -current + oldCurrent;
        } else if (oldOp == '*') {
            current *= oldCurrent;
        } else {
            current = oldCurrent / current;
        }
        return current;
    }

    int calculate(string s) {
        int current = 0;
        unordered_map<char, int> priority = {
            {'+', 0},
            {'-', 0},
            {'*', 1},
            {'/', 1}
        };

        for (char c : s) {
            if (isdigit(c)) {
                current *= 10;
                current += c - '0';
            } else if (c == '+' || c == '-' || c == '*' || c == '/') {
                while (!opStack.empty() && priority[opStack.top()] >= priority[c]) {
                    current = calculation(current);
                }
                numStack.push(current);
                opStack.push(c);
                current = 0;
            }
        }

        while (!opStack.empty()) {
            current = calculation(current);
        }

        return current;
    }

private:
    stack<int> numStack;
    stack<char> opStack;
};

// @lc code=end

