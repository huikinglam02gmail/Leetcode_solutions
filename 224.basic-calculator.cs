/*
 * @lc app=leetcode id=224 lang=csharp
 *
 * [224] Basic Calculator
 */

// @lc code=start
public class Solution {
    public int Calculate(string s) 
    {
        int current = 0;
        int result = 0;
        Stack<int> resultStack = new Stack<int>();
        Stack<bool> signStack = new Stack<bool>();
        bool positive = true;

        foreach (char c in s)
        {
            if (Char.IsDigit(c))
            {
                current *= 10;
                current += c - '0';
            }
            else if (c == '+' || c == '-' || c == ')')
            {
                if (positive)
                {
                    result += current;
                }
                else
                {
                    result -= current;
                }
                current = 0;
                if (c == '+' || c == '-')
                {
                    positive = (c == '+');
                }
                else
                {
                    bool prevSign = signStack.Pop();
                    int prevResult = resultStack.Pop();
                    if (prevSign)
                    {
                        prevResult += result;
                    }
                    else
                    {
                        prevResult -= result;
                    }
                    result = prevResult;
                }
            }
            else if (c == '(')
            {
                resultStack.Push(result);
                signStack.Push(positive);
                current = 0;
                result = 0;
                positive = true;
            }
        }
        if (current != 0)
        {
            if (positive)
            {
                result += current;
            }
            else
            {
                result -= current;
            }
        }
        return result;
    }
}
// @lc code=end

