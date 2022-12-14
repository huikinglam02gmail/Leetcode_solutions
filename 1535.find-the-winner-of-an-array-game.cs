/*
 * @lc app=leetcode id=1535 lang=csharp
 *
 * [1535] Find the Winner of an Array Game
 */

// @lc code=start
public class Solution 
{
    public int GetWinner(int[] arr, int k) 
    {
        Stack<int> stack = new Stack<int>();
        int n = arr.Length;
        int arrMax = arr.Max(x => x);
        if (k >= n)
        {
            return arrMax;
        }
        for (int i = n-1; i >= 0; i--)
        {
            stack.Push(arr[i]);
        }
        int win = 0;
        while (win < k && stack.Peek() < arrMax)
        {
            int last = stack.Pop();
            int secondLast = stack.Pop();
            if (last > secondLast)
            {
                win++;
                stack.Push(last);
            }
            else
            {
                win = 1;
                stack.Push(secondLast);
            }
        }
        return stack.Peek();
    }
}
// @lc code=end

