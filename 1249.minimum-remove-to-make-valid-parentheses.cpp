/*
 * @lc app=leetcode id=1249 lang=cpp
 *
 * [1249] Minimum Remove to Make Valid Parentheses
 */

// @lc code=start
#include <string>
#include <stack>
#include <unordered_set>

class Solution {
public:
    /*
    Keep a stack to find if each parenthesis is valid
    In a stack, we keep the indices of open and close parenthesis [i, 1] or [i,-1]
    When a new parenthesis come in, we ask if it can close previous open parenthesis that results in a pop. The successful closes will be recorded as good parenthesis    
    */
    std::string minRemoveToMakeValid(std::string s) {
        std::stack<std::pair<int, int>> stack;
        std::unordered_set<int> good;
        
        for (int i = 0; i < s.size(); i++) {
            char c = s[i];
            if (c == '(') {
                stack.push(std::make_pair(i, 1));
            } else if (c == ')') {
                if (!stack.empty() && stack.top().second == 1) {
                    auto item = stack.top();
                    stack.pop();
                    good.insert(item.first);
                    good.insert(i);
                } else {
                    stack.push(std::make_pair(i, -1));
                }
            }
        }
        
        std::string result;
        for (int i = 0; i < s.size(); i++) {
            char c = s[i];
            if (isalpha(c) || good.count(i) > 0) {
                result += c;
            }
        }
        
        return result;
    }
};

// @lc code=end

