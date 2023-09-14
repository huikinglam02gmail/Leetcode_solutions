/*
 * @lc app=leetcode id=1896 lang=cpp
 *
 * [1896] Minimum Cost to Change the Final Value of Expression
 */

// @lc code=start
#include <vector>
#include <stack>
#include <algorithm>

using std::vector;

class Solution {
public:
    /*
    Notice the rules:
    '&' does not take precedence over '|' in the order of calculation.
    Evaluate parentheses first, then in left-to-right order.
    So first deal with parentheses first, use stack to hold the calculated expression
    When we calculate, we record what the original value is. And the minimum cost to flip it to 1 - value
    Because parentheses can occur on the RHS, we have these scenarios:
    exp1 op exp2
    1. 0 & 0 -> 1 + min(cost(exp1), cost(exp2))
    2. 0 | 0 -> min(cost(exp1), cost(exp2))
    3. 0 & 1 -> 1
    4. 0 | 1 -> 1
    5. 1 & 0 -> 1
    6. 1 | 0 -> 1
    7. 1 & 1 -> min(cost(exp1), cost(exp2))
    8. 1 | 1 -> 1 + min(cost(exp1), cost(exp2))
    */
    std::vector<int> FlipCost(std::vector<int>& left, char op, std::vector<int>& right) {
        if (op == '!') {
            return right;
        }
        else {
            int newValue;
            if (op == '&') {
                newValue = (left[0] > 0 && right[0] > 0) ? 1 : 0;
            }
            else {
                newValue = (left[0] > 0 || right[0] > 0) ? 1 : 0;
            }

            int newCost;
            if (left[0] != right[0]) {
                newCost = 1;
            }
            else {
                newCost = std::min(left[1], right[1]);
                if ((op == '&' && left[0] == 0) || (op == '|' && left[0] == 1)) {
                    newCost += 1;
                }
            }

            return { newValue, newCost };
        }
    }

    int minOperationsToFlip(std::string expression) {
        std::stack<std::vector<int>> stack;
        std::stack<char> stackOp;
        std::vector<int> current = { -1, 0 };
        char currentOp = '!';

        for (char c : expression) {
            if (c == '&' || c == '|') {
                currentOp = c;
            }
            else if (c == '(') {
                stack.push(current);
                stackOp.push(currentOp);
                current = { -1, 0 };
                currentOp = '!';
            }
            else if (c == ')') {
                std::vector<int> leftTuple = stack.top();
                stack.pop();
                char leftOp = stackOp.top();
                stackOp.pop();
                current = FlipCost(leftTuple, leftOp, current);
            }
            else {
                vector<int> t {c - '0', 1};
                current = FlipCost(current, currentOp, t);
            }
        }

        return current[1];
    }
};
// @lc code=end

