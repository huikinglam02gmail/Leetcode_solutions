/*
 * @lc app=leetcode id=1499 lang=csharp
 *
 * [1499] Max Value of Equation
 */

// @lc code=start
public class Solution 
{
    public int FindMaxValueOfEquation(int[][] points, int k) 
    {
        PriorityQueue<int, int> heap = new PriorityQueue<int, int>();
        int result = Int32.MinValue;
        foreach (int[] item in points)
        {
            int x = item[0];
            int y = item[1];
            while (heap.TryPeek(out int xj, out int diff) && x - xj > k)
            {
                int item1 = heap.Dequeue();
            }
            if (heap.TryPeek(out int xj1, out int diff1))
            {
                result = Math.Max(result, x + y - diff1);
            }
            heap.Enqueue(x, x- y);
        }
        return result;   
    }
}
// @lc code=end

