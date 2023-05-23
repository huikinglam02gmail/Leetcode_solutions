/*
 * @lc app=leetcode id=703 lang=csharp
 *
 * [703] Kth Largest Element in a Stream
 */

// @lc code=start
using System.Collections.Generic;
public class KthLargest 
{
    PriorityQueue<int, int> pq;
    int size;
    public KthLargest(int k, int[] nums) 
    {
        pq = new PriorityQueue<int, int>();
        size = k;
        foreach (int num in nums)
        {
            pq.Enqueue(num, num);
            while (pq.Count > k)
            {
                pq.Dequeue();
            }
        }
    }
    
    public int Add(int val) 
    {
        pq.Enqueue(val, val);
        if (pq.Count > size)
        {
            pq.Dequeue();
        }
        return pq.Peek();
    }
}

/**
 * Your KthLargest object will be instantiated and called as such:
 * KthLargest obj = new KthLargest(k, nums);
 * int param_1 = obj.Add(val);
 */
// @lc code=end

