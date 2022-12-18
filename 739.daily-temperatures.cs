/*
 * @lc app=leetcode id=739 lang=csharp
 *
 * [739] Daily Temperatures
 */

// @lc code=start
public class Solution 
{
    public int[] DailyTemperatures(int[] temperatures) 
    {
        int n = temperatures.Length;
        int[] result = new int[n];
        Stack<int> stack = new Stack<int>();

        Array.Fill(result, 0);
        for (int i = n - 1; i >= 0; i--)
        {
            while (stack.Count > 0 && temperatures[stack.Peek()] <= temperatures[i])
            {
                stack.Pop();
            }
            if (stack.TryPeek(out int ind))
            {
                result[i] = ind - i;
            }
            stack.Push(i);
        }
        return result;
    }
}
// @lc code=end

