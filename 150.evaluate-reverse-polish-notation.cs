/*
 * @lc app=leetcode id=150 lang=csharp
 *
 * [150] Evaluate Reverse Polish Notation
 */

// @lc code=start
public class Solution 
{
    public int EvalRPN(string[] tokens) 
    {
        if (tokens.Length == 1)
        {
            return Int32.Parse(tokens[0]);
        }
        else
        {
            Stack<int> stack = new Stack<int>();
            foreach (string token in tokens)
            {
                if (token != "+" && token != "-" && token != "*" && token != "/")
                {
                    stack.Push(Int32.Parse(token));
                }
                else
                {
                    int right = stack.Pop();
                    int left = stack.Pop();
                    if (token == "+")
                    {
                        left += right;
                    }
                    else if (token  == "-")
                    {
                        left -= right;
                    }
                    else if (token == "*")
                    {
                        left *= right;
                    }
                    else
                    {
                        left /= right;
                    }
                    stack.Push(left);
                }
            }
            return stack.Peek();
        }
    }
}
// @lc code=end

