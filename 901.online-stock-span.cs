/*
 * @lc app=leetcode id=901 lang=csharp
 *
 * [901] Online Stock Span
 */

// @lc code=start
public class StockSpanner {

    Stack<int[]> stack = new Stack<int[]>();
    int count;
    public StockSpanner() 
    {
        stack.Push(new int[2] {100001, -1});
        count = 0;
    }
    
    public int Next(int price) 
    {
        int ans = 1;
        while (price >= stack.Peek()[0])
        {
            stack.Pop();
            ans = count - stack.Peek()[1];
        }
        stack.Push(new int[] {price, count});
        count += 1;
        return ans;
    }
}

/**
 * Your StockSpanner object will be instantiated and called as such:
 * StockSpanner obj = new StockSpanner();
 * int param_1 = obj.Next(price);
 */
// @lc code=end

