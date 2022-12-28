/*
 * @lc app=leetcode id=1962 lang=csharp
 *
 * [1962] Remove Stones to Minimize the Total
 */

// @lc code=start
public class Solution 
{
    public int MinStoneSum(int[] piles, int k) 
    {
        PriorityQueue<int, int> heap = new PriorityQueue<int, int>();
        foreach (int pile in piles)
        {
            heap.Enqueue(pile, - pile);

        }

        for (int i = 0; i < k; i++)
        {
            int item = heap.Dequeue();
            item = item - item / 2;
            heap.Enqueue(item, - item);
        }

        int result = 0;
        while (heap.TryDequeue(out int pile, out int priority))
        {
            result += pile;
        }
        return result;
    }
}
// @lc code=end

