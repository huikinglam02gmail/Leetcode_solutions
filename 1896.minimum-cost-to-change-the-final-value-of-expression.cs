/*
 * @lc app=leetcode id=1896 lang=csharp
 *
 * [1896] Minimum Cost to Change the Final Value of Expression
 */

// @lc code=start
public class Solution {
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
    private int[] FlipCost(int[] left, char op, int[] right) {
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
                newCost = Math.Min(left[1], right[1]);
                if ((op == '&' && left[0] == 0) || (op == '|' && left[0] == 1)) {
                    newCost += 1;
                }
            }

            return new int[] { newValue, newCost };
        }
    }

    public int MinOperationsToFlip(string expression) {
        Stack<int[]> stack = new Stack<int[]>();
        Stack<char> stackOp = new Stack<char>();
        int[] current = new int[] { -1, 0 };
        char currentOp = '!';

        foreach (char c in expression) {
            if (c == '&' || c == '|') {
                currentOp = c;
            }
            else if (c == '(') {
                stack.Push(current);
                stackOp.Push(currentOp);
                current = new int[] { -1, 0 };
                currentOp = '!';
            }
            else if (c == ')') {
                int[] leftTuple = stack.Pop();
                char leftOp = stackOp.Pop();
                current = FlipCost(leftTuple, leftOp, current);
            }
            else {
                current = FlipCost(current, currentOp, new int[] { c - '0', 1 });
            }
        }

        return current[1];
    }
}

// @lc code=end

