/*
 * @lc app=leetcode id=2019 lang=cpp
 *
 * [2019] The Score of Students Solving Math Expression
 */

// @lc code=start
#include <unordered_map>
#include <unordered_set>
#include <stack>
#include <string>

using namespace std;

class Solution {
private:
    unordered_map<string, unordered_set<int>> memo;

    unordered_set<int> DP(string s) {
        if (s.find('+') == string::npos && s.find('*') == string::npos) {
            return { stoi(s) };
        } else {
            if (memo.count(s)) {
                return memo[s];
            }

            vector<int> opIndices;
            for (int i = 0; i < s.length(); i++) {
                if (s[i] == '+' || s[i] == '*') {
                    opIndices.push_back(i);
                }
            }

            unordered_set<int> result;
            for (int i : opIndices) {
                unordered_set<int> lSet = DP(s.substr(0, i));
                unordered_set<int> rSet = DP(s.substr(i + 1));
                for (int l : lSet) {
                    for (int r : rSet) {
                        if (s[i] == '+' && l + r <= 1000) {
                            result.insert(l + r);
                        }
                        if (s[i] == '*' && l * r <= 1000) {
                            result.insert(l * r);
                        }
                    }
                }
            }

            memo[s] = result;
            return result;
        }
    }

    stack<int> numStack;
    stack<char> opStack;

    int Calculation(int current) {
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

public:
    int Calculate(string s) {
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
                    current = Calculation(current);
                }
                numStack.push(current);
                opStack.push(c);
                current = 0;
            }
        }

        while (!opStack.empty()) {
            current = Calculation(current);
        }

        return current;
    }

    int scoreOfStudents(string s, vector<int>& answers) {
        unordered_map<int, int> possibleAnswers;
        possibleAnswers[Calculate(s)] = 5;
        unordered_set<int> wrongAnswers = DP(s);

        for (int ans : wrongAnswers) {
            if (!possibleAnswers.count(ans)) {
                possibleAnswers[ans] = 2;
            }
        }

        int result = 0;
        for (int ans : answers) {
            result += possibleAnswers.count(ans) ? possibleAnswers[ans] : 0;
        }

        return result;
    }
};

// @lc code=end

