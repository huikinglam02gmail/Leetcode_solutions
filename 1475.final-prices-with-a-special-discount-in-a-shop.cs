/*
 * @lc app=leetcode id=1475 lang=csharp
 *
 * [1475] Final Prices With a Special Discount in a Shop
 */

// @lc code=start
public class Solution 
{
    public int[] FinalPrices(int[] prices) 
    {
        Stack<int> stack = new Stack<int>();
        int n = prices.Length;
        for (int i = 0; i < n; i++)
        {
            while (stack.TryPeek(out int top) && prices[top] >= prices[i])
            {
                prices[stack.Pop()] -= prices[i];
            }
            stack.Push(i);
        }
        return prices;
    }
}
// @lc code=end

