/*
 * @lc app=leetcode id=239 lang=csharp
 *
 * [239] Sliding Window Maximum
 */

// @lc code=start
using System.Collections.Generic;
using System.Linq;
class MonotonicDecreasingQueue
{
    private LinkedList<int[]> queue;
    public MonotonicDecreasingQueue(int[] nums)
    {
        queue = new LinkedList<int[]>();
        for (int i = 0; i < nums.Length; i++)
        {
            insert(nums[i], i);
        }
    }

    public void insert(int value, int index)
    {
        while (queue.Count > 0 && queue.Last.Value[0] < value)
        {
            queue.RemoveLast();
        }
        queue.AddLast(new int[2] {value, index});
    }

    public int[] peek()
    {
        if (queue.Count > 0)
        {
            return queue.First.Value;
        }
        else
        {
            return new int[2] {-1, -1};
        }
    }

    public void dequeue()
    {
        queue.RemoveFirst();
    }
}
public class Solution 
{
    public int[] MaxSlidingWindow(int[] nums, int k) 
    {
        MonotonicDecreasingQueue MDQ = new MonotonicDecreasingQueue(nums.Take(k).ToArray());
        List<int> result = new List<int>();
        result.Add(MDQ.peek()[0]);
        for (int i = k; i < nums.Length; i++)
        {
            if (i == k + MDQ.peek()[1])
            {
                MDQ.dequeue();
            }
            MDQ.insert(nums[i], i);
            result.Add(MDQ.peek()[0]);
        }
        return result.ToArray();
    }
}
// @lc code=end

