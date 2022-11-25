/*
 * @lc app=leetcode id=907 lang=csharp
 *
 * [907] Sum of Subarray Minimums
 */

// @lc code=start
public class Solution 
{
    public int SumSubarrayMins(int[] arr) 
    {
        Stack<int> stack = new Stack<int>();
        List<long> dp = new List<long>();
        List<int> newArr = new List<int>();
        long MOD = 1000000007;
        long result = 0;
        newArr.Add(0);
        for (int i = 0; i < arr.Length; i++)
        {
            newArr.Add(arr[i]);
        }

        for (int i = 0; i < newArr.Count; i++)
        {
            if (i == 0)
            {
                dp.Add(newArr[i]);
            }
            else
            {
                while (newArr[i] < newArr[stack.Peek()])
                {
                    stack.Pop();
                }
                dp.Add(dp[stack.Peek()] + (i - stack.Peek())*newArr[i]);
            }
            stack.Push(i);
            dp[i] %= MOD;
            result += dp[i];
            result %= MOD;
        }
        return (int) result;
    }
}
// @lc code=end

