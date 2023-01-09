/*
 * @lc app=leetcode id=1599 lang=csharp
 *
 * [1599] Maximum Profit of Operating a Centennial Wheel
 */

// @lc code=start
public class Solution {
    public int MinOperationsMaxProfit(int[] customers, int boardingCost, int runningCost) 
    {
        int profit = 0;
        int maxSoFar = 0;
        int result = -1;
        int waiting = 0;
        int turn = 0;
        while (turn < customers.Length || waiting > 0)
        {
            if (turn < customers.Length)
            {
                waiting += customers[turn];
            }
            int board = Math.Min(4, waiting);
            profit += board * boardingCost - runningCost;
            if (profit > maxSoFar)
            {
                maxSoFar = profit;
                result = turn + 1;
            }
            waiting -= board;
            turn++;
        }    
        return result;
    }
}
// @lc code=end

