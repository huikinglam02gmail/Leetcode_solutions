/*
 * @lc app=leetcode id=1753 lang=csharp
 *
 * [1753] Maximum Score From Removing Stones
 */

// @lc code=start
using System;
using System.Collections.Generic;

public class Solution 
{
    public int MaximumScore(int a, int b, int c) 
    {
        PriorityQueue<int, int> heap = new PriorityQueue<int,int>();
        heap.Enqueue(a, -a);
        heap.Enqueue(b, -b);
        heap.Enqueue(c, -c);
        int result = 0;
        
        while (heap.Count >= 2) 
        {
            int x = heap.Dequeue();
            int y = heap.Dequeue();
            
            if (heap.Count > 0) 
            {
                int z = heap.Peek();
                result += y - z + 1;
                x -= (y - z + 1);
                y = z - 1;
                
                if (y > 0) 
                {
                    heap.Enqueue(y, -y);
                }
                
                if (x > 0) 
                {
                    heap.Enqueue(x, -x);
                }
            } 
            else 
            {
                result += y;
            }
        }       
        return result;
    }
}

// @lc code=end

