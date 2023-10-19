/*
 * @lc app=leetcode id=844 lang=cpp
 *
 * [844] Backspace String Compare
 */

// @lc code=start
/**
 * @lc app=leetcode id=844 lang=cpp
 *
 * [844] Backspace String Compare
 */

#include <string>
#include <stack>
using namespace std;

class Solution {
public:
    bool backspaceCompare(string s, string t) {
        stack<char> sFinal, tFinal;

        for (char c : s) {
            if (c == '#') {
                if (!sFinal.empty()) {
                    sFinal.pop();
                }
            } else {
                sFinal.push(c);
            }
        }

        for (char c : t) {
            if (c == '#') {
                if (!tFinal.empty()) {
                    tFinal.pop();
                }
            } else {
                tFinal.push(c);
            }
        }

        if (sFinal.size() != tFinal.size()) {
            return false;
        }

        while (!sFinal.empty()) {
            if (sFinal.top() != tFinal.top()) {
                return false;
            }
            sFinal.pop();
            tFinal.pop();
        }

        return true;
    }
};

// @lc code=end

